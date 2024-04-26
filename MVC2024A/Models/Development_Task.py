from Models.Task_Model import Task

class DevelopmentTask(Task):
    def __init__(self, description, developer):
        super().__init__(description, developer, "Desarrollo")
