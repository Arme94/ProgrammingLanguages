
class TaskView:

    def __init__(self):
        pass

    def getMenu(self):
        print("Menú de tareas")
        print("1. Mostrar todas las tareas")
        print("2. Cambiar estado de tarea")
        print("3. Agregar tarea")
        print("4. Salir")
        return input("Ingrese una opción:")

    def showAllTasks(self, tasks:list):
        print("Lista de tareas")
        for index, task in enumerate(tasks):
            print(f"{index} - {task.getDescription()} - {task.getFinished()}")

    def getUserInput(self):
        return input("Ingrese el índice de la tarea:")

    def changeState(self, task, state):
        task.setState(state)


    def addTask(self, newTask):
        pass

    