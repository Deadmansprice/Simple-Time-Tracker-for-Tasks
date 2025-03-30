from datetime import datetime

class Task:
    def __init__(self, name):
        self.name = name  # Task name
        self.total_time = 0  # Total time in seconds
        self.sessions = []

    def add_session(self, start, end):
        duration = (end - start).total_seconds()
        self.total_time += duration
        self.sessions.append((start, end))

    def to_dict(self):
        return {
            "name": self.name,
            "total_time": self.total_time,
            "sessions": [
                {"start": s.isoformat(), "end": e.isoformat()} for s, e in self.sessions
            ]
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["name"])
        task.total_time = data["total_time"]
        task.sessions = [
            (datetime.fromisoformat(session["start"]), datetime.fromisoformat(session["end"]))
            for session in data["sessions"]
        ]
        return task