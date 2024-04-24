from Models.Development_Task import DevelopmentTask
from Models.Testing_Task import TestingTask
class TaskFactory:
    def create_task(self, description, duration, project, developer, finished, task_type, state):
        pass

class DevelopmentTaskFactory(TaskFactory):
    def create_task(self, description, duration, project, developer, finished, state):
        return DevelopmentTask(description, duration, project, developer, finished, state)

class TestingTaskFactory(TaskFactory):
    def create_task(self, description, duration, project, developer, finished, state):
        return TestingTask(description, duration, project, developer, finished, state)
