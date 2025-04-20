from flask import Flask, render_template, request, redirect, jsonify
from database import init_db, add_task, get_task, get_tasks, update_task, delete_task, start_session, stop_session, get_active_session, stop_active_session
from datetime import datetime
import csv

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    tasks = get_tasks()
    categories = sorted(list(set(task.category for task in tasks if task.category)))
    return render_template('index.html', tasks=tasks, categories=categories)

@app.route('/add_task', methods=['POST'])
def add_task_route():
    name = request.form['name']
    priority = request.form['priority']
    category = request.form['category']
    notes = request.form['notes']
    add_task(name, priority, category, notes)
    return redirect('/')

@app.route('/edit_task/<int:task_id>', methods=['POST'])
def edit_task_route(task_id):
    name = request.form['name']
    priority = request.form['priority']
    category = request.form['category']
    notes = request.form['notes']
    update_task(task_id, name, priority, category, notes)
    return redirect('/')

@app.route('/delete_task/<int:task_id>')
def delete_task_route(task_id):
    delete_task(task_id)
    return redirect('/')

@app.route('/start_timer/<int:task_id>')
def start_timer(task_id):
    session_id = start_session(task_id)
    return jsonify({'session_id': session_id})

@app.route('/stop_timer/<int:task_id>')
def stop_timer(task_id):
    stop_active_session(task_id)
    return jsonify({'status': 'stopped'})

@app.route('/get_timer/<int:task_id>')
def get_timer(task_id):
    task = get_task(task_id)
    active_session = get_active_session(task_id)
    total_completed_time = sum(session.duration() for session in task.sessions if session.end_time)
    if active_session:
        active_start_time = active_session.start_time.isoformat()
    else:
        active_start_time = None
    return jsonify({'total_completed_time': total_completed_time, 'active_start_time': active_start_time})

@app.route('/export_csv')
def export_csv():
    tasks = get_tasks()
    with open('tasks.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Priority', 'Category', 'Notes', 'Total Time'])
        for task in tasks:
            writer.writerow([task.name, task.priority, task.category, task.notes, task.total_time])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)