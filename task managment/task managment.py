task = []
# function to show all tasks
def show_task():
    #checking if the task is empty 
    if len(task) == 0:
        print("No task to show..")
    else:
        #if the task is not empty . looping through the list and displaying rach task wiith its number
        for i, task_item in enumerate(task , 1):
            print(f"{i}, {task_item}")

# function to add new task 
def add_task ():
    #user to enter the task
    new_num = input("Enter your task")
    #creating new task to take a list..
    task.append(new_num)
    #conforming the task
    print(f"Task {new_num} wad added ")

# function to delete the task
def delete_task():
    #showing the user to delete the task 
    show_task()
    del_num = int (input("Enter the task to delete.."))
    #removing the tasken choosen by user 
    new_num = task.pop(del_num - 1)
    print(f" Task {del_num} was delted")

    #   Main loop
while True:
    #displaying the manu option

    print("\n 1. Show task "  " \n2 . Add task " " \n3. Delete Task " " \n4. Quit")
    choice = input("Enter your choice ")

    if choice == '1':
        show_task()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Good byee....")
        break
    else:
        print("Invalid try again")



    




  
