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
            self.tasks[taskIndex].finishTask()
        else:
            print("Id de tarea no válido")

    def showAllTasks(self):
        #llamar método en la vista:
        self.view.showAllTasks(self.tasks)

    def runController(self):

        #mostrar todas las tareas en la vista:
        # self.view.showAllTasks(self.tasks)

        # #capturar entrada de la vista
        # task_id = self.view.getUserInput()

        # #actualizar el modelo
        # if task_id.isdigit():
        #     task_id = int(task_id)
        #     if 0 <= task_id < len(self.tasks):
        #         self.toggle_task_fin(task_id)
        #         self.showAllTasks()
        #     else:
        #         print("Id de tarea no válido")
        # else:
        #     print("Id de tarea no válido")
        while True:
            option = self.view.getMenu()
            if option == "1":
                self.showAllTasks()
            elif option == "2":
                self.view.showFinishedTasks(self.tasks)
            elif option == "3":
                self.view.showUnfinishedTasks(self.tasks)
            elif option == "4":
                task_id = self.view.getUserInput()
                if task_id.isdigit():
                    task_id = int(task_id)
                    if 0 <= task_id < len(self.tasks):
                        self.toggle_task_fin(task_id)
                    else:
                        print("Id de tarea no válido")
                else:
                    print("Id de tarea no válido")
            elif option == "5":
                task_desc = input("Ingrese la descripción de la tarea:")
                task_duration = input("Ingrese la duración de la tarea:")
                task_project = input("Ingrese el proyecto de la tarea:")
                task_developer = input("Ingrese el desarrollador de la tarea:")

                new_task = Task_Model.Task(task_desc, task_duration, task_project, task_developer)
                self.add_task(new_task)
            elif option == "6":
                break
            else:
                print("Opción no válida")

    

        

