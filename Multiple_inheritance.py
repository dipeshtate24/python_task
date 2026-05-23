class Employee:
    company = "Visa"
    ecode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgrade_level(self):
        self.level = self.level + 1


class Programmer(Employee, Freelancer):
    name = "Rohit"

p = Programmer()
p.upgrade_level()
print(p.level)
print(p.company)

class Employee:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(f"The name of Empolyee is {self.name}")
        

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def showDance(self):
        print(f"The performing dance form is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

o = DancerEmployee('Kathak', 'Pooja')
o.showName()
o.showDance()
print(DancerEmployee.mro())
