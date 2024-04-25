class TaskView:

    def __init__(self):
        pass

    def getMenu(self):
        print("Menú de tareas")
        print("1. Mostrar todas las tareas")
        print("2. Mostrar tareas finalizadas")
        print("3. Mostrar tareas pendientes")
        print("4. Finalizar tarea")
        print("5. Agregar tarea")
        print("6. Salir")
        return input("Ingrese una opción:")

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

    