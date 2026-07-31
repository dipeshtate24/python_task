class Number:
    def sum(self):
        return self.a + self.b
    
num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)

"""
PascaleCase
EmpolyeeName

camelCase
isNumeric, isFloat

"""
class RailwayForm:
    fromType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

Application = RailwayForm()
Application.name = "Soham"
Application.train = "Rajdhani Express"

Application.printData()


class Employee():
    company = "Google"
    salary = 100

Suresh = Employee()
Rajni = Employee()

Suresh.salary = 300
Rajni.salary = 400

print(Suresh.company)
print(Rajni.company)

# Employee.company = "Youtube"

# print(Suresh.company)
# print(Rajni.company)
Suresh.salary = 45
print(Suresh.salary)
print(Rajni.salary)


class Employee:
    company = 'Google'
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} and salary is {self.salary}")

    def greet(self):
        print(f'Good Morning, {self.name}')


Person = Employee()
Person.salary = 100000
Person.name = 'Suresh'
Person.getSalary()
Person.greet()

class Employee:
    company = 'Google'
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} and salary is {self.salary}.\n{signature}")

    @staticmethod
    def greet():
        print(f'Good Morning, Everyone')

    @staticmethod
    def time():
        print("The time is 9 AM in the morning")

Person = Employee()
Person.salary = 100000
Person.name = 'Suresh'
Person.getSalary("Thanks!")
Person.greet()
Person.time()


class Employee:
    company = 'Google'

    def __init__(self, name, salary, subnit):
        self.name = name
        self.salary = salary
        self.subnit = subnit
        print("Employee is created.")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subnit of the employee is {self.subnit}")
    
    def getSalary(name, salary):
        print(f"Salary for this employee working in {name} and salary is {salary}.")

    @staticmethod
    def greet():
        print(f'Good Morning, Everyone')

    @staticmethod
    def time():
        print("The time is 9 AM in the morning")

Person1 = Employee("Ramesh", 100, "Youtube")
Person1.getDetails()
