import json
import argparse

# Load task data from tasks.json
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save task data to tasks.json
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

# Add a new task
def add_task(task_description):
    tasks = load_tasks()
    tasks.append({'task': task_description, 'completed': False})
    save_tasks(tasks)
    print(f"Task added: {task_description}")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['completed'] else "✗"
            print(f"{i}. {task['task']} [{status}]")

# Complete a task
def complete_task(task_number):
    tasks = load_tasks()
    try:
        tasks[task_number - 1]['completed'] = True
        save_tasks(tasks)
        print(f"Task {task_number} marked as complete!")
    except IndexError:
        print("Invalid task number")

# Remove a task
def remove_task(task_number):
    tasks = load_tasks()
    try:
        task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task removed: {task['task']}")
    except IndexError:
        print("Invalid task number")

# Main program
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    parser.add_argument("command", choices=['add', 'list', 'complete', 'remove'])
    parser.add_argument("value", nargs='?', help="Task description or task number")

    args = parser.parse_args()

    if args.command == "add":
        if args.value:
            add_task(args.value)
        else:
            print("Please provide a task description.")
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        if args.value and args.value.isdigit():
            complete_task(int(args.value))
        else:
            print("Please provide a valid task number.")
    elif args.command == "remove":
        if args.value and args.value.isdigit():
            remove_task(int(args.value))
        else:
            print("Please provide a valid task number.")

if __name__ == "__main__":
    main()
