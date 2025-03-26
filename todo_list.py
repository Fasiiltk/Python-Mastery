# todo_list.py
tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)
    elif choice == "4":
        break
    else:
        print("Invalid choice")