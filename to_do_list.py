import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    else:
        return {"tasks": []}

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, description, priority="medium", due_date=""):
    tasks["tasks"].append({
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    })
    save_tasks(tasks)

def remove_task(tasks, index):
    if 0 <= index < len(tasks["tasks"]):
        del tasks["tasks"][index]
        save_tasks(tasks)
    else:
        print("Invalid task index!")

def complete_task(tasks, index):
    if 0 <= index < len(tasks["tasks"]):
        tasks["tasks"][index]["completed"] = True
        save_tasks(tasks)
    else:
        print("Invalid task index!")

def display_tasks(tasks):
    print("\nTasks:")
    for index, task in enumerate(tasks["tasks"], start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['description']} - Priority: {task['priority']}, Due Date: {task['due_date']}")

def main():
    # Load existing tasks or initialize an empty list
    tasks = load_tasks()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date = input("Enter due date (optional): ")
            add_task(tasks, description, priority, due_date)

        elif choice == "2":
            display_tasks(tasks)
            index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(tasks, index)

        elif choice == "3":
            display_tasks(tasks)
            index = int(input("Enter the index of the task to complete: ")) - 1
            complete_task(tasks, index)

        elif choice == "4":
            display_tasks(tasks)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
