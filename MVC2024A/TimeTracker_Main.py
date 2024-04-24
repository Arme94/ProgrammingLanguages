

from Controllers import Task_Controller
from Strategies.Strategy import DevelopmentStateChangeStrategy

if __name__ == "__main__":
    myTaskController = Task_Controller.TaskController(DevelopmentStateChangeStrategy)
    myTaskController.runController()
    