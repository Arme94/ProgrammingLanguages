from Models.Task_Model import Task

class StateChangeStrategy:
    def change_state(self, task:Task, new_state):
        pass

class DevelopmentStateChangeStrategy(StateChangeStrategy):
    def change_state(self, task, new_state):
        if task.task_type == "Desarrollo":
            task.state = new_state

class TestingStateChangeStrategy(StateChangeStrategy):
    def change_state(self, task, new_state):
        if task.task_type == "Testing":
            task.state = new_state