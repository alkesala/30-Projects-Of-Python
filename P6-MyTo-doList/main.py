import json
import datetime
"""TODO LIST"""

"""What to do:
1. Create a list of tasks
2. Add a task to the list
3. Delete a task from the list
4. View the list of tasks
5. Exit the program
6. Save the tasks to a file
7. Load the tasks from a file
8. Mark a task as complete
9. De-mark a task as complete
10. View completed tasks
11. View uncompleted tasks
12. View all tasks
13. Time stamp tasks
"""

class Task:
    def __init__ (self, task):
        self.task = task
        self.task_id = 0
        self.task_time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed = False
        
    def __str__ (self):
        status = "Completed" if self.completed else "Uncompleted"
        return f"[{status}] ({self.task_id}) {self.task} - Created: {self.task_time_stamp}"
    
    def remove_task(self):
        self.task = ""
        self.completed = False
        
    def complete_task(self):
        self.completed = True
        
    def uncomplete_task(self):
        self.completed = False