class Task:
    def __init__(self,taskname, task_description, task_duration):   
        self.taskname=taskname
        self.task_description = task_description
        self.task_duration = task_duration
        self.task_completed = False

    def completed(self):
        self.task_completed=True

    def __str__(self):
        taskCompleted = "yes" if self.task_completed else "no"
        return f"Task name: {self.taskname}, task description: {self.task_description},task duration: {self.task_duration}, task completed: {taskCompleted}"
    






class ToDoList:
    
    def __init__(self):
        self.tasks = []

    def add_task(self, taskname, task_description, task_duration):
        task=Task(taskname, task_description, task_duration)
        self.tasks.append(task)

    def view_task(self):
        if not self.tasks:
            print( "empty")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print (f"task Id: {i}, {task}")
    
    def mark_task_as_completed(self,task_index):
        if 1 <= task_index <=len (self.tasks):
            task_to_mark = self.tasks[task_index-1]
            task_to_mark.completed()
            print(f"task{task_to_mark.taskname} marked as completed")

        else:
            print("invalid task id")

 

def main():
    my_list = ToDoList()

    while True:     
        print("================================")
        print("1: view tasks ")
        print("2: add task ")
        print("3: mark task as completed ")
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
            TaskID= int(input("enter the task number to mark as completed"))
            my_list.mark_task_as_completed(TaskID)

        else:
            print("option not available")

if __name__ == "__main__":
    main()
