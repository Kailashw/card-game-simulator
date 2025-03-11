
import time

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add(self, name, delay):
        self.tasks.append((name, delay))
    
    def execute(self):
        for task in self.tasks:
            time.sleep(task[1])
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {task[0]}")