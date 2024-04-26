from Models.Engineer_Model import Engineer

class DeveloperEngineer(Engineer):
    def __init__(self, name):
        super().__init__(name, "Developer")
    