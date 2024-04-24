from Models.Task_Model import Task

class DevelopmentTask(Task):
    def __init__(self, description, duration, project, developer, finished, state):
        super().__init__(description, duration, project, developer, finished, "Desarrollo")
        self.state = state