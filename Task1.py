# Simple To-Do List Application in Python

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")

def update_task(task_number, new_task):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = new_task
        print(f"Task {task_number} updated to '{new_task}'.")
    else:
        print("Invalid task number.")

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_number = int(input("Enter the task number to delete: "))
        delete_task(task_number)
    elif choice == '4':
        task_number = int(input("Enter the task number to update: "))
        new_task = input("Enter the new task: ")
        update_task(task_number, new_task)
    elif choice == '5':
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")
