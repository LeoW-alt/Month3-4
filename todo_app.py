#Simple To Do list CLI App
from datetime import datetime

FILENAME = "tasks.txt"
DATE_FORMAT = "%Y-%m-%d"

#Loading the tasks from the files if they are there
def load_tasks():
    tasks = []

    try:
        #Try to open the file in read mode
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    tasks.append({
                        "name": parts[0],
                        "due_date": parts[1],
                        "status": parts[2]
                    })
    except FileNotFoundError:
        pass

    return tasks

#Saves the tasks on the file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
       for task in tasks:
        file.write(f"{task['name']}|{task['due_date']}|{task['status']}\n")   

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. View by status")
    print("4. Edit a task")
    print("5. Mark task as complete")
    print("6. Remove a task")
    print("7. Exit")
    
def display_tasks(tasks):
    print(f"\n{'#':<4} {'Task':<30} {'Due Date':<15} {'Status'}")
    print("-" * 60)
    for i, task in enumerate(tasks, start=1):
        print(f"{i:<4} {task['name']:<30} {task['due_date']:<15} {task['status']}")

def get_valid_date():
    while True:
        due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ").strip()
        if due_date == "":
            return "No due date"
        try:
            datetime.strptime(due_date, DATE_FORMAT)
            return due_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def view_by_status(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n  Filter by:")
    print("  1. Pending")
    print("  2. Complete")
    filter_choice = input("  Choose (1 or 2): ").strip()
 
    if filter_choice == "1":
        filtered = [t for t in tasks if t["status"] == "Pending"]
        label = "Pending"
    elif filter_choice == "2":
        filtered = [t for t in tasks if t["status"] == "Complete"]
        label = "Complete"
    else:
        print("  Invalid choice.")
        return
 
    print(f"\n--- {label} Tasks ---")
    if not filtered:
        print(f"  No {label.lower()} tasks found.")
    else:
        display_tasks(filtered)            

def edit_task(task):
    if not tasks:
        print("No tasks to edit.")
        return
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to edit: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
 
    task = tasks[task_number - 1]
    print(f"\nEditing task: '{task['name']}' — press Enter to keep current value.")
 
    new_name = input(f"  New name [{task['name']}]: ").strip()
    if new_name:
        task["name"] = new_name
 
    task["due_date"] = get_valid_date(current=task["due_date"])
 
    save_tasks(tasks)
    print(f"  Task updated successfully.")
 

def mark_complete(tasks):
    if not tasks:
        print("No tasks to mark as complete.")
        return
    display_tasks(tasks)
    try:
        ask_number = int(input("Enter the task number to mark as complete: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
        elif tasks[task_number - 1]["status"] == "Complete":
            print(f"  '{tasks[task_number - 1]['name']}' is already marked as complete.")
        else:
            tasks[task_number - 1]["status"] = "Complete"
            save_tasks(tasks)
            print(f"  Marked '{tasks[task_number - 1]['name']}' as complete.")
    except ValueError:
        print("Please enter a valid number.")

tasks = load_tasks()

#Runs until exit option is chosen
while True:
    show_menu()
    choice = input("Choose an option(1-7): ").strip()

    if choice == "1":
        name = input("Enter a new task: ").strip()
        if not name:
            print("Task name cannot be empty.")
        else:
            due_date = get_valid_date()
            tasks.append({"name": name, "due_date": due_date, "status": "Pending"})
            save_tasks(tasks)
            print("Task added and saved.")    

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            display_tasks(tasks)

    elif choice == "3":
        view_by_status(tasks)  

    elif choice == "4":
        edit_task(tasks)

    elif choice == "5":
        mark_complete(tasks)          

    elif choice == "6":
        if not tasks:
            print("No tasks to remove.")
        else:
            display_tasks(tasks)    
            try:
                task_number = int(input("Enter the task number to remove: "))
                if task_number < 1 or task_number > len(tasks):
                    print("Invalid task number.")
                else:
                    removed_task = tasks.pop(task_number - 1)     
                    save_tasks(tasks)
                    print(f"Removed task: {removed_task['name']}")
            except ValueError:
                print("Please enter a valid number.")                           

    elif choice == "7":
        print("Bye")
        break                         

    else:
        print("Invalid choice. Please select 1, 2, 3, 4 or 5")                        