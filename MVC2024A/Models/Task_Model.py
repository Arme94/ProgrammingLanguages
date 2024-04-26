from Models.Engineer_Model import Engineer

class Task:

    def __init__(self, description, engineer: Engineer, typeTask):
        self.description = description
        self.engineer = engineer
        self.type = typeTask
        self.finished = False
        self.state = "inicio"

    def finishTask(self):
        self.finished = True

    def getFinished(self):
        return self.finished
    
    def getDescription(self):
        return self.description

    def getengineer(self):
        return self.engineer
    
    def getState(self):
        return self.state
    


