
class EngineerView:

    def __init__(self):
        pass

    def getMenu(self):
        print("Menú de ingenieros")
        print("1. Mostrar todas los ingenieros")
        print("2. Agregar ingeniero")
        print("3. Salir")
        return input("Ingrese una opción:")

    def showAllEngineers(self, engineers:list):
        print("Lista de ingenieros")
        for index, engineer in enumerate(engineers):
            print(f"{index} - {engineer.get_name()} - {engineer.get_role()}")

    def getUserInput(self):
        return input("Ingrese el índice del ingeniero:")

    def addEngineer(self, newEngineer):
        pass