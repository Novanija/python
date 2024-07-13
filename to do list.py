# To-Do List Manager

# Initialize an empty list to store tasks
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to complete: "))
            complete_task(task_index)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
