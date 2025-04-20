# Simple Time Tracker

## Overview

Simple Time Tracker is a web-based application designed to help users manage and track the time spent on various tasks. Built with Flask, SQLite, HTML, CSS, and JavaScript, it offers a responsive interface that works on both desktop and mobile devices. The app supports task creation, time tracking, categorization, and CSV export, with a focus on user-friendly features like theme switching and task filtering.

## Features

- **Task Management**: Add, delete, and track tasks with details like name, priority, category, and notes.
- **Time Tracking**: Start, stop, and reset timers for each task, with time displayed in a detailed format (e.g., "1 minute 30 seconds").
- **Categories**: Assign categories to tasks, with a dropdown menu that auto-populates existing categories for reuse.
- **Filtering**: Filter tasks by category or priority for better organization.
- **Theme Toggle**: Switch between dark and light themes, with preferences saved in `localStorage`.
- **CSV Export**: Export task data (name, priority, category, notes, total time) to a CSV file.
- **Responsive Design**: Adapts to different screen sizes, ensuring usability on mobile and desktop.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/simple-time-tracker.git
   cd simple-time-tracker
   ```

2. Set Up a Virtual Environment (optional but recommended)

   ```bash
	python -m venv venv
	source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
 
3. Install Dependencies:
   ```bash
	pip install flask
   ```
4. Initialize the Database:
 - The database (tasks.db) is automatically created when you run the app for the first time.

 5. Run the Application:
	```bash
	python app.py
   ```
 - Open your browser and navigate to http://127.0.0.1:5000.

## Usage
1. Add a Task:
 - Enter a task name, select a priority (low, medium, high), choose or type a category, and add optional notes.
 - Click "Add Task" to save it.

2. Track Time:
 - Use the "Start" button to begin tracking time for a task.
 - Click "Stop" to pause the timer, and "Reset" to set the displayed time back to 0 (note: reset is currently client-side only).
 - Time is displayed in a detailed format (e.g., "1 minute 30 seconds").

3. Filter Tasks:
 - Use the dropdown menus to filter tasks by category or priority.
 - Click "Apply Filters" to update the task list (filter logic implementation pending).

4. Export Data:
 - Click "Export to CSV" on any task to download a CSV file containing all tasks (currently saves to the server; download functionality pending).

5. Switch Themes:
 - Click the "Settings" button in the top-right corner.
 - Select "Dark" or "Light" theme from the dropdown.