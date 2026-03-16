## Month3-4
# Simple To-Do List CLI App

A lightweight command-line to-do list application written in Python. Tasks are saved to a local text file so they persist between sessions.

## Features

- Add tasks with optional due dates
- View all tasks in a formatted table
- Filter tasks by status (Pending or Complete)
- Edit an existing task's name or due date
- Mark tasks as complete (with duplicate-check)
- Remove tasks by number
- Persistent storage via a local `tasks.txt` file

## Requirements

- Python 3.x (no external libraries required)

## Getting Started

1. Clone or download the repository.
2. Run the app from your terminal:

```bash
python todo_app.py
```
## Usage

The menu is shown before every action:
```
--- TO-DO LIST MENU ---
1. Add a task
2. View all tasks
3. View by status
4. Edit a task
5. Mark task as complete
6. Remove a task
7. Exit
```

### 1. Add a Task
Enter a task name, then optionally provide a due date in `YYYY-MM-DD` format. Press Enter to skip the due date. New tasks are always created with a `Pending` status.

### 2. View All Tasks
Displays every saved task in a table showing the task number, name, due date, and status.

### 3. View by Status
Filter and display only `Pending` or `Complete` tasks via a short sub-menu.

### 4. Edit a Task
Select a task by number and update its name and/or due date. Press Enter on any field to keep the current value.

### 5. Mark Task as Complete
Select a task by number to set its status to `Complete`. If the task is already complete, you'll be notified and no change will be made.

### 6. Remove a Task
Select a task by number to permanently delete it from the list.

### 7. Exit
Exits the application.

## Data Storage

Tasks are stored in a plain text file called `tasks.txt` in the same directory as the script. Each line represents one task in the format:

```
task_name|due_date|status
```

This file is created automatically on first use and updated whenever tasks are added, edited, removed, or completed.
