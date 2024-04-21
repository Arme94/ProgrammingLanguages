from Models.Task_Model import Task

class Development(Task):
    def __init__(self, description, duration, project, developer):
        super().__init__(description, duration, project, developer)
        self.task_type = "development"

class Testing(Task):
    def __init__(self, description, duration, project, developer):
        super().__init__(description, duration, project, developer)
        self.task_type = "testing"

class TaskFactory:
    def create_task(self, task_type, description, duration, project, developer):
        if task_type == "development":
            return Development(description, duration, project, developer)
        elif task_type == "testing":
            return Testing(description, duration, project, developer)
        else:
            return Task(description, duration, project, developer)