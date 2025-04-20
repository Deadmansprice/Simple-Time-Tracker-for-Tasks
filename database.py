import sqlite3
from datetime import datetime
from models import Task, Session

def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS tasks
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     priority TEXT DEFAULT 'medium',
                     notes TEXT,
                     total_time REAL DEFAULT 0)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS sessions
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     task_id INTEGER,
                     start_time TEXT,
                     end_time TEXT,
                     FOREIGN KEY(task_id) REFERENCES tasks(id))''')
    cursor = conn.execute("PRAGMA table_info(tasks)")
    columns = [col[1] for col in cursor.fetchall()]
    if 'category' not in columns:
        conn.execute('ALTER TABLE tasks ADD COLUMN category TEXT')
    conn.commit()
    conn.close()

def add_task(name, priority, category, notes):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (name, priority, category, notes) VALUES (?, ?, ?, ?)', (name, priority, category, notes))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return [Task(**task) for task in tasks]

def get_task(task_id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    sessions = conn.execute('SELECT * FROM sessions WHERE task_id = ?', (task_id,)).fetchall()
    conn.close()
    if task:
        task_obj = Task(**task)
        task_obj.sessions = [Session(**session) for session in sessions]
        return task_obj
    return None

def update_task(task_id, name, priority, category, notes):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET name = ?, priority = ?, category = ?, notes = ? WHERE id = ?', (name, priority, category, notes, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM sessions WHERE task_id = ?', (task_id,))
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def start_session(task_id):
    conn = get_db_connection()
    start_time = datetime.now().isoformat()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sessions (task_id, start_time) VALUES (?, ?)', (task_id, start_time))
    conn.commit()
    session_id = cursor.lastrowid
    conn.close()
    return session_id

def stop_session(session_id):
    conn = get_db_connection()
    end_time = datetime.now().isoformat()
    conn.execute('UPDATE sessions SET end_time = ? WHERE id = ?', (end_time, session_id))
    conn.commit()
    conn.close()

def get_active_session(task_id):
    conn = get_db_connection()
    session = conn.execute('SELECT * FROM sessions WHERE task_id = ? AND end_time IS NULL', (task_id,)).fetchone()
    conn.close()
    return Session(**session) if session else None

def stop_active_session(task_id):
    conn = get_db_connection()
    active_session = conn.execute('SELECT id FROM sessions WHERE task_id = ? AND end_time IS NULL', (task_id,)).fetchone()
    if active_session:
        session_id = active_session['id']
        end_time = datetime.now().isoformat()
        conn.execute('UPDATE sessions SET end_time = ? WHERE id = ?', (end_time, session_id))
        conn.commit()
    conn.close()

def reset_task_time(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET total_time = 0 WHERE id = ?', (task_id,))
    conn.execute('DELETE FROM sessions WHERE task_id = ?', (task_id,))
    conn.commit()
    conn.close()