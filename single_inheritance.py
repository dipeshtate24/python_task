class Employee:
    company = "Google"

    def show_details(self):
        print("This is an employee.")

    
class Programmer(Employee):
    language = "Python"
    
    def get_language(self):
        print(f"The language is {self.language}")

    def show_details(self):
        print("This is a Programmer.")
    
e = Employee()
e.show_details()
p = Programmer()
p.get_language()
p.show_details()
print(p.company)

class Employee:
    company = "Camel"
    salary = 100
    location = "Pune"


    # def change_salary(self, sal):
    #     self.salary = sal

    # def change_salary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def change_salary(self, sal):
        self.salary = sal

e = Employee()
print(e.salary)
e.change_salary(200)
print(e.salary)
print(Employee.salary)