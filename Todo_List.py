print("TODO LIST")
print("Enter : \n1. Add Task \n2. Delete Task \n3. Mark as Completed \n4. Show Tasks \n5. Exit")

tasks = []
status = []

while True:
    try:
        choice = int(input("\nEnter your Choice: "))
        if choice == 1:
            task = input("Enter the Task: ").strip()
            if task:
                tasks.append(task)
                status.append(False)  # False means not completed
            else:
                print("Task cannot be empty.")

        elif choice == 2:
            if not tasks:
                print("No tasks to delete.")
            else:
                task_num = int(input("Enter Task Number to Delete: "))
                if 1 <= task_num <= len(tasks):
                    tasks.pop(task_num - 1)
                    status.pop(task_num - 1)
                    print("Task deleted successfully.")
                else:
                    print("Invalid task number.")

        elif choice == 3:
            if not tasks:
                print("No tasks to mark.")
            else:
                task_num = int(input("Enter Task Number to Mark as Completed: "))
                if 1 <= task_num <= len(tasks):
                    status[task_num - 1] = True  # Mark as completed
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")

        elif choice == 4:
            if not tasks:
                print("No tasks available.")
            else:
                print("\nTask Number | Task Description | Status")
                print("-" * 50)
                for i, (task, stat) in enumerate(zip(tasks, status), start=1):
                    print(f"{i:<11} | {task:<20} | {'Completed' if stat else 'Pending'}")

        elif choice == 5:
            print("Exiting the TODO list program. Have a great day!")
            break

        else:
            print("Invalid choice, please enter a number between 1 and 5.")

    except ValueError:
        print("Invalid input! Please enter a number.")
