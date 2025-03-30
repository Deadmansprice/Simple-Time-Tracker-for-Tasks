import tkinter as tk
from tkinter import simpledialog, messagebox
from time_tracker import TimeTracker
from utils import format_time
from datetime import datetime

class TimeTrackerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Time Tracker")
        self.tracker = TimeTracker()
        self.tracker.load_from_file("time_tracker_data.json")

        self.current_timer_label = tk.Label(self, text="No task is being timed")
        self.current_timer_label.pack()

        self.task_listbox = tk.Listbox(self, selectmode='single', activestyle='none')
        self.task_listbox.pack(expand=True, fill='both')

        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side='left')

        self.toggle_timer_button = tk.Button(self, text="Start Timer", command=self.toggle_timer, state='disabled')
        self.toggle_timer_button.pack(side='left')

        self.delete_task_button = tk.Button(self, text="Delete Task", command=self.delete_task, state='disabled')
        self.delete_task_button.pack(side='left')

        self.task_listbox.bind('<<ListboxSelect>>', self.on_task_select)
        self.task_listbox.bind('<Double-1>', self.rename_task)  # Double click to rename tasks

        self.update_timer()  # Starts timer updates

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handles window close

    def update_task_list(self):
        # Get the currently selected task name, if any
        selected_task_name = None
        selected_index = self.task_listbox.curselection()
        if selected_index and 0 <= selected_index[0] < len(self.tracker.tasks): #Ensure index is valid
            selected_task_name = self.tracker.tasks[selected_index[0]].name

        # Clear and update the listbox
        self.task_listbox.delete(0, 'end')
        for task in self.tracker.tasks:
            display_time = self.tracker.get_display_time(task)
            display_str = f"{task.name} - {format_time(display_time)}"
            self.task_listbox.insert('end', display_str)

        # Re-select the task if it still exists
        if selected_task_name:
            for i, task in enumerate(self.tracker.tasks):
                if task.name == selected_task_name:
                    self.task_listbox.select_set(i)
                    break

    def update_timer(self):
        if self.tracker.current_task is not None and self.tracker.start_time is not None:
            current_duration = (datetime.now() - self.tracker.start_time).total_seconds()
            display_str = f"Timing: {self.tracker.current_task.name} - {format_time(current_duration)}"
            self.current_timer_label.config(text=display_str)
        else:
            self.current_timer_label.config(text="No task is being timed")
        self.update_task_list()
        self.after(1000, self.update_timer)

    def add_task(self):
        name = simpledialog.askstring("Add Task", "Enter task name:")
        if name:
            self.tracker.add_task(name)
            self.update_task_list()

    def toggle_timer(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tracker.tasks[selected_index[0]]
            if self.tracker.current_task == task:
                self.tracker.stop_timer()
                self.toggle_timer_button.config(text="Start Timer")
            else:
                self.tracker.start_timer(task)
                self.toggle_timer_button.config(text="Stop Timer")
            self.update_task_list()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tracker.tasks[selected_index[0]]
            try:
                self.tracker.remove_task(task)
                self.update_task_list()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def on_task_select(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.toggle_timer_button.config(state='normal')
            self.delete_task_button.config(state='normal')
            task = self.tracker.tasks[selected_index[0]]
            if self.tracker.current_task == task:
                self.toggle_timer_button.config(text="Stop Timer")
            else:
                self.toggle_timer_button.config(text="Start Timer")
        else:
            self.toggle_timer_button.config(state='disabled')
            self.delete_task_button.config(state='disabled')

    def rename_task(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tracker.tasks[selected_index[0]]
            new_name = simpledialog.askstring("Rename Task", "Enter new name:", initialvalue=task.name)
            if new_name:
                task.name = new_name
                self.update_task_list()

    def on_closing(self):
        self.tracker.save_to_file("time_tracker_data.json")
        self.destroy()  # Handles window close

if __name__ == "__main__":
    app = TimeTrackerGUI()
    app.mainloop()