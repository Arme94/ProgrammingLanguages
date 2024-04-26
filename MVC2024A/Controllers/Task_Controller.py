from Views import Task_View
from Models.Development_Task import DevelopmentTask
from Models.Testing_Task import TestingTask
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

    def showAllTasks(self):
        #llamar método en la vista:
        self.view.showAllTasks(self.tasks)

    def runController(self):

        while True:
            option = self.view.getMenu()
            if option == "1":
                self.showAllTasks()
            elif option == "2":
                pass
                ##self.showFinishedTasks()
            elif option == "3":                
                task_type = input("Ingrese el tipo de tarea (D/T):")
                if task_type == "D":
                    task_desc = input("Ingrese la descripción de la tarea:")
                    task_developer = input("Ingrese el desarrollador de la tarea:")
                    new_task = DevelopmentTask(task_desc, task_developer)
                    self.add_task(new_task)
                elif task_type == "T":
                    task_desc = input("Ingrese la descripción de la tarea:")
                    task_developer = input("Ingrese el desarrollador de la tarea:")
                    new_task = TestingTask(task_desc, task_developer, "Testing")
                    self.add_task(new_task)
                else:
                    print("Tipo de tarea no válido")
                
            elif option == "4":
                break
            else:
                print("Opción no válida")

    

        

