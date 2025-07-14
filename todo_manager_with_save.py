import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    """Add a new task to the list."""
    tasks.append({"task": task, "completed": False})
    print(f"Added task: {task}")
    save_tasks(tasks)

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for idx, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx + 1}. [{status}] {task['task']}")

def mark_complete(tasks, task_index):
    try:
        task = tasks[task_index - 1]
        task["completed"] = True
        print(f"Task '{task['task']}' marked as complete.")
        save_tasks(tasks)
    except IndexError:
        print("Invalid task number.")

def remove_task(tasks, task_index):
    try:
        removed = tasks.pop(task_index - 1)
        print(f"Removed task: '{removed['task']}'")
        save_tasks(tasks)
    except IndexError:
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Manager (with Save) ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "3":
            view_tasks(tasks)
            try:
                num = int(input("Enter task number to mark as complete: "))
                mark_complete(tasks, num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            view_tasks(tasks)
            try:
                num = int(input("Enter task number to remove: "))
                remove_task(tasks, num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Exiting program. Saving tasks...")
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()