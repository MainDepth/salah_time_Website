# add a feature that stores the list of tasks into .txt file

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

