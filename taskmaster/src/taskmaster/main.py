import json
import os
import sys
from rich.console import Console
from rich.table import Table

# Define the path for JSON storage
JSON_STORAGE_PATH = os.path.expanduser("~/.taskmaster.json")

# Initialize console for rich UI
console = Console()

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(JSON_STORAGE_PATH):
        with open(JSON_STORAGE_PATH, 'r') as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(JSON_STORAGE_PATH, 'w') as file:
        json.dump(tasks, file)

# Display tasks in a rich table
def display_tasks(tasks):
    table = Table(title="TaskMaster Tasks")
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Task", style="magenta")
    table.add_column("Status", justify="center", style="green")

    for idx, task in enumerate(tasks):
        status = "✔️" if task.get("completed", False) else "❌"
        table.add_row(str(idx + 1), task["name"], status)

    console.print(table)

# Add a new task
def add_task(task_name):
    tasks = load_tasks()
    tasks.append({"name": task_name, "completed": False})
    save_tasks(tasks)
    console.print(f"Task '{task_name}' added successfully!", style="bold green")

# Complete a task
def complete_task(task_id):
    tasks = load_tasks()
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1]["completed"] = True
        save_tasks(tasks)
        console.print(f"Task {task_id} marked as completed!", style="bold green")
    else:
        console.print("Invalid task ID!", style="bold red")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    if 0 < task_id <= len(tasks):
        removed_task = tasks.pop(task_id - 1)
        save_tasks(tasks)
        console.print(f"Task '{removed_task['name']}' deleted successfully!", style="bold green")
    else:
        console.print("Invalid task ID!", style="bold red")

# Main function to handle CLI commands
def main():
    if len(sys.argv) < 2:
        console.print("Usage: taskmaster [add|list|complete|delete] [options]", style="bold yellow")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 3:
        add_task(sys.argv[2])
    elif command == "list":
        tasks = load_tasks()
        display_tasks(tasks)
    elif command == "complete" and len(sys.argv) == 3:
        complete_task(int(sys.argv[2]))
    elif command == "delete" and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]))
    else:
        console.print("Invalid command or arguments!", style="bold red")

if __name__ == "__main__":
    main()