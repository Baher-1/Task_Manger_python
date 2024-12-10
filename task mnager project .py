tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Task added: {task}")

def view_tasks():
    print("\nCurrent tasks:")
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks available.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task deleted: {removed_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\nChoose an option:")
    print("1 - Add Task")
    print("2 - View Tasks")
    print("3 - Delete Task")
    print("4 - Exit")

    choice = input("Enter choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        