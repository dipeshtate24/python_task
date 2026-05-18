class Employee:
    def __init__(self, name):
        self.name = name

    def showDetails(self):
        print(f"The name of Employee is {self.name}.")

a = Employee('Superman')
a.showDetails()
Employee.showDetails(a)