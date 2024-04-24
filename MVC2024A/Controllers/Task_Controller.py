from Views import Task_View
from Models import Task_Model
from Strategies.Strategy import DevelopmentStateChangeStrategy, TestingStateChangeStrategy

class TaskController:

    def __init__(self, state_strategy):

        #referencia al modelo:
        self.tasks = []
        #referencia a la vista 
        self.view = Task_View.TaskView()
        self.state_strategy = state_strategy()

    def add_task(self, task):
        self.tasks.append(task)

    def toggle_task_fin(self, taskIndex):
        if 0 <= taskIndex < len(self.tasks):
            self.tasks[taskIndex].toogleFinished()
        else:
            print("Id de tarea no válido")

    def showAllTasks(self):
        #llamar método en la vista:
        self.view.showAllTasks(self.tasks)

    def runController(self):

        #mostrar todas las tareas en la vista:
        self.view.showAllTasks(self.tasks)

        #capturar entrada de la vista
        task_id = self.view.getUserInput()

        #actualizar el modelo
        if task_id.isdigit():
            task_id = int(task_id)
            if 0 <= task_id < len(self.tasks):
                self.toggle_task_fin(task_id)
                self.showAllTasks()
            else:
                print("Id de tarea no válido")
        else:
            print("Id de tarea no válido")

    

        

