#file handling with text file
#create a tast
#view a task 
#exet program
# append_example.py

def menu():
    print("=========================")
    print("Please Select one option")
    print("1: Add new tak")
    print("2: view task")
    print("3: Delete task")
    print("0: Exit")
    print("=========================")

tasks = []

def add_task(task):
    task = input("Enter a new task: ")
    tasks.append(task)

def show_tasks():
    if tasks:
        for i, t in enumerate(tasks, start=1):
            print(i, t)
    else:
        print("No task Avalable")
def del_task():
    user_input = int(input("Enter task no. you want to delete: "))
    tasks.pop(user_input -1)
    print(f"{user_input} is deleted successfully")
    
    
while(True):
    try:
        menu()
        user_input = int(input("=>"))
        if user_input == 1:
            add_task(tasks)
        elif user_input == 2:
            show_tasks()
        elif user_input == 3:
            del_task()
        elif user_input == 0:
            break
        else:
            print("invalid input")
    except:
        print("Please Select the correct option")
        
