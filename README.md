# Simple Time Tracker for Tasks

A minimalistic time tracking application built with Python and Tkinter. This application allows you to create, manage, and track the time spent on tasks, with data persistence using a local JSON file.

## Features

- **Add Tasks**: Create new tasks by clicking the "Add Task" button on the left side and entering a task name.
- **Edit Tasks**: Rename existing tasks by double-clicking on them in the list.
- **Delete Tasks**: Remove tasks by selecting a task and clicking the "Delete Task" button (note: you cannot delete a task that is currently being timed).
- **Track Time**: Start and stop a timer for a task by selecting it and clicking "Start Timer" (which toggles to "Stop Timer" while active).
- **Automatic Save**: Tasks and their total times are automatically saved to a `time_tracker_data.json` file when you close the application window.
- **Load on Launch**: On re-launch, the application loads existing tasks from the `time_tracker_data.json` file, if it exists.
- **Local Data Storage**: All data is stored locally in a human-readable JSON file, which you can review externally.

## Requirements

- Python 3.12 or higher
- Tkinter (usually included with Python; if not, install it via your package manager, e.g., `sudo apt-get install python3-tk` on Linux)

## How to Run

1. Clone the repository:
git clone https://github.com/your-username/Simple-Time-Tracker-for-Tasks.git
cd Simple-Time-Tracker-for-Tasks

2. Navigate to the `Source` directory:

3. Run the application:
python gui.py

Alternatively, you can open the project in Visual Studio and run `main.py`.

## Project Structure

- `Source/`: Contains the main application files.
- `gui.py`: The main GUI implementation using Tkinter.
- `main.py`: Entry point to run the application.
- `task.py`: Defines the `Task` class for managing task data.
- `time_tracker.py`: Manages task logic and timer functionality.
- `utils.py`: Utility functions, such as time formatting.
- `time_tracker_data.json`: Automatically generated file that stores task data (not tracked by Git).

## Notes

- This is a Minimum Viable Product (MVP) with basic functionality. Future improvements could include enhanced UI styling, additional features like task categories, or more robust error handling.
- The application is designed to be simple and lightweight, with all data stored locally in a JSON file for easy review.

## License

This project is open-source and available under the [MIT License](LICENSE).