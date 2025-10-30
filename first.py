tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for i, t in enumerate(tasks, start=1):
        print(i, t)

while True:
    choice = input("1:Add 2:View 3:Exit -> ")
    if choice == "1":
        add_task(input("Task: "))
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")