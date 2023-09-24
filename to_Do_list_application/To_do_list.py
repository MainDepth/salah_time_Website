import To_do_list_class 

# add a feature that stores the list of tasks into .txt file

def main():
    my_list = To_do_list_class.ToDoList()

    while True:     
        print("================================")
        print("1: view tasks ")
        print("2: add task ")
        print("3: mark task as completed ")
        print("4: save tasks")
        print("5: load tasks")
        print("================================")

        a =input("Select an option ")



        if a == "1":
           my_list.view_task()

        elif a == "2": 
            name = input(str("name of task: "))
            desctription = input(str("task description: "))
            duration = input(str("duration of task: "))
            my_list.add_task(name,desctription, duration)

        elif a == "3":
            TaskID= int(input("enter the task number to mark as completed: "))
            my_list.mark_task_as_completed(TaskID)

        else:
            print("option not available")

if __name__ == "__main__":
    main()