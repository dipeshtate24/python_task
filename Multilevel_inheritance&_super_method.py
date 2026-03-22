class Person:

    def __init__(self):
        print("Initializing the person ...\n")

    country = "India"

    def takeBreak(self):
        print("I am breathing....")

class Employee(Person):

    def __init__(self):
        super().__init__()
        print("Initializing the employee ...\n")

    company = "Honda"

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreak(self):
        print("I am employee and I am taking break.")

class Programmer(Employee):

    company = 'Fiverr'
    
    def __init__(self):
        super().__init__()
        print("Initializing the programmer ...\n")


    def getSalary(self):
        print(f"Salary to programmer.")

    def takeBreak(self):
        super().takeBreak()
        print("I am employee and take breath.")

p = Person()
p.takeBreak()
print(p.country)
e = Employee()
print(e.company)
e.takeBreak()
pr = Programmer()
pr.getSalary()
pr.takeBreak()
