# task_manager.py
# Yeh program user ke tasks ko tasks.txt file me save karta hai

FILENAME = "tasks.txt"

def menu():
    print("\n=========================")
    print(" Simple Task Manager ")
    print("=========================")
    print("1: Add new task")
    print("2: View all tasks")
    print("3: Delete a task")
    print("0: Exit")
    print("=========================")

def add_task():
    task = input("Enter a new task: ")
    # 'a' = append mode (purane data ko delete nahi karega)
    with open(FILENAME, "a") as f:
        f.write(task + "\n")
    print(f"✅ Task '{task}' saved to {FILENAME}")

def show_tasks():
    try:
        with open(FILENAME, "r") as f:
            tasks = f.readlines()
        if tasks:
            print("\n📋 Your Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t.strip()}")
        else:
            print("⚠️ No tasks available.")
    except FileNotFoundError:
        print("⚠️ No tasks file found yet.")

def del_task():
    try:
        with open(FILENAME, "r") as f:
            tasks = f.readlines()

        show_tasks()
        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            with open(FILENAME, "w") as f:
                f.writelines(tasks)
            print(f"🗑️ Task '{removed.strip()}' deleted successfully.")
        else:
            print("❌ Invalid task number.")
    except FileNotFoundError:
        print("⚠️ No tasks file found yet.")
    except ValueError:
        print("❌ Please enter a valid number.")

# ---------- Main Loop ----------
while True:
    menu()
    choice = input("=> ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        del_task()
    elif choice == "0":
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again.")
