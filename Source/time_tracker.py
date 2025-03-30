import json
from datetime import datetime
from task import Task

class TimeTracker:
    def __init__(self):
        self.tasks = []
        self.current_task = None
        self.start_time = None

    def add_task(self, name):
        new_task = Task(name)
        self.tasks.append(new_task)

    def start_timer(self, task):
        if task in self.tasks:
            if self.current_task is not None:
                self.stop_timer()
            self.current_task = task
            self.start_time = datetime.now()

    def stop_timer(self):
        if self.current_task is not None and self.start_time is not None:
            elapsed_time = (datetime.now() - self.start_time).total_seconds()
            self.current_task.total_time += elapsed_time
            self.current_task = None
            self.start_time = None

    def remove_task(self, task):
        if task == self.current_task:
            raise ValueError("Cannot delete a task that is currently being timed.")
        if task in self.tasks:
            self.tasks.remove(task)

    def get_display_time(self, task):
        if task == self.current_task and self.start_time is not None:
            return task.total_time + (datetime.now() - self.start_time).total_seconds()
        return task.total_time

    def save_to_file(self, filename):
        try:
            data = [task.to_dict() for task in self.tasks]
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Successfully saved tasks to {filename}")
        except Exception as e:
            print(f"Failed to save tasks to {filename}: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
        except FileNotFoundError:
            self.tasks = []