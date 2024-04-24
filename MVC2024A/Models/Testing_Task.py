from Models.Task_Model import Task

class TestingTask(Task):
    def __init__(self, description, duration, project, developer, finished, state):
        super().__init__(description, duration, project, developer, finished, "Testing")
        self.state = state