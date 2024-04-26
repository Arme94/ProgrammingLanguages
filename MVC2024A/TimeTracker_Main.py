from Controllers import Task_Controller, Engineer_Controller
from Strategies.Strategy import DevelopmentStateChangeStrategy

if __name__ == "__main__":
    while True:
        print("1. Operar ingenieros")
        print("2. Operar tareas")
        print("3. Salir")
        option = input("Ingrese una opción:")
        if option == "1":
            engineController = Engineer_Controller.EngineerController()
            engineController.runController()
        elif option == "2":
            myTaskController = Task_Controller.TaskController(DevelopmentStateChangeStrategy)
            myTaskController.runController()
        elif option == "3":
            break
        else:
            print("Opción no válida")    
    