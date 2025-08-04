import os
def save_all_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    tasks=[]
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
              tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_task(tasks):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def display_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.\n")
    else:
        print("your tasks:")    
        for idx, task in enumerate(tasks, start = 1):
            print(f"{idx}. {task}")
        print()

tasks = load_tasks()

while True:
    print("To-Do List Menu")
    print("1.  Add Task")
    print("2.  View All Tasks")
    print("3.  Delete task")
    print("4.  Update task")
    print("5.  Exit")
    choice = input("Enter your choice(1-5): ")
    if choice == '1':
        task = input("Enter your task: ")
        tasks.append(task)
        save_task(task)
        print("Task added successfully!\n")
    elif choice == '2':
        display_tasks(tasks)
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to delete.\n")
        else:
            display_tasks(tasks)
            try:
                task_num =int(input("Enter the task number to delete: "))
                if 1<= task_num <=len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_all_tasks(tasks) 
                    print("f Task '{removed}' deleted successfully!\n") 
                else:
                    print("Invalid task number.\n")
            except ValueError :
                print("Please enter a valid number.\n")  


    elif choice == '4':
        if len(tasks) == 0:
            print("No tasks to update.\n")
        else:
            display_tasks(tasks)
            try:
                task_num = int(input("Enter the task no to update: "))
                if 1 <= task_num <= len(tasks):
                    new_task = input("Enter the updated task: ")
                    tasks[task_num - 1]= new_task
                    save_all_tasks(tasks)
                    print("Task updated successfully.\n")
                else:
                    print("invalid task.\n")
            except ValueError:
                print("please enter a valid no.\n")

    elif choice == '5':
        print("Exiting To-Do list. GoodBye!")
        break
    else:
        print("Invalid choice. Please enter 1-3.\n")        

