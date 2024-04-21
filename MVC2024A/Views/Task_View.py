class TaskView:

    def __init__(self):
        pass

    def showAllTasks(self, tasks:list):
        print("Lista de tareas")
        for index, task in enumerate(tasks):
            print(f"{index} - {task.getDescription()} - {task.getFinished()}")

    def showFinishedTasks(self, tasks: list):
        print("Tareas finalizadas")
        for task in tasks:
            if task.getFinished():
                print(task.getDescription())

    def showUnfinishedTasks(self, tasks):
        print("Tareas pendientes")
        for task in tasks:
            if not task.getFinished():
                print(task.getDescription())

    def getUserInput(self):
        return input("Ingrese el índice de la tarea:")

    def finishTask(self, numTask):
        pass

    def addTask(self, newTask):
        pass

    