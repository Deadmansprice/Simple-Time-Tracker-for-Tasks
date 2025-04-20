from datetime import datetime

class Task:
    def __init__(self, id, name, priority='medium', category='', notes='', total_time=0):
        self.id = id
        self.name = name
        self.priority = priority
        self.category = category
        self.notes = notes
        self.total_time = total_time
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)
        self.total_time += session.duration()

class Session:
    def __init__(self, id, task_id, start_time, end_time=None):
        self.id = id
        self.task_id = task_id
        self.start_time = datetime.fromisoformat(start_time) if isinstance(start_time, str) else start_time
        self.end_time = datetime.fromisoformat(end_time) if end_time and isinstance(end_time, str) else end_time

    def duration(self):
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0