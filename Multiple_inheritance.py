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