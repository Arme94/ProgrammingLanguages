from Models.Engineer_Model import Engineer

class DeveloperEngineer(Engineer):
    def __init__(self, name):
        super().__init__(name, "developer")

class QAEngineer(Engineer):
    def __init__(self, name):
        super().__init__(name, "QA")

class EngineerFactory:
    def create_engineer(self, role, name):
        if role == "developer":
            return DeveloperEngineer(name)
        elif role == "QA":
            return QAEngineer(name)
        else:
            return Engineer(name, role)