class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def ShowDetails(self):
        print(f"The name of Employee is {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python")

e1 = Employee("Rohan Kumar", "E1")
e1.ShowDetails()
e2 = Programmer("Pankaj Das", "E2")
e2.ShowDetails()
e2.showLanguage()