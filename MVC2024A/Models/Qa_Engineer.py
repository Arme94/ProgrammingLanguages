from Models.Engineer_Model import Engineer

class QaEngineer(Engineer):
    def __init__(self, name):
        super().__init__(name, "QA")