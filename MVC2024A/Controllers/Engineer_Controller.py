from Views import Engineer_View
from Models.Qa_Engineer import QaEngineer
from Models.Developer_Engineer import DeveloperEngineer

class EngineerController:

    def __init__(self):
        self.engineers = []
        self.view = Engineer_View.EngineerView()

    def add_engineer(self, engineer):
        self.engineers.append(engineer)
    
    def showAllEngineers(self):
        self.view.showAllEngineers(self.engineers)

    def runController(self):
        while True:
            option = self.view.getMenu()
            if option == "1":
                self.showAllEngineers()
            elif option == "2":
                engineer_type = input("Ingrese el tipo de ingeniero (D/Q):")
                if engineer_type == "D":
                    engineer_name = input("Ingrese el nombre del ingeniero:")
                    new_engineer = DeveloperEngineer(engineer_name)
                    self.add_engineer(new_engineer)
                elif engineer_type == "Q":
                    engineer_name = input("Ingrese el nombre del ingeniero:")
                    new_engineer = QaEngineer(engineer_name)
                    self.add_engineer(new_engineer)
                else:
                    print("Tipo de ingeniero no válido")
            elif option == "3":
                break
            else:
                print("Opción no válida")