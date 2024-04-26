from Models.Task_Model import Task
from Models.Qa_Engineer import QaEngineer

class TestingTask(Task):
    def __init__(self, description, engineer: QaEngineer):
        super().__init__(description, engineer, "Testing")