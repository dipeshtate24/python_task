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

    def change_salary(self, sal):
        self.salary = sal

    def change_salary(self, sal):
        self.__class__.salary = sal

    @classmethod
    def change_salary(self, sal):
        self.salary = sal

e = Employee()
print(e.salary)
e.change_salary(200)
print(e.salary)
print(Employee.salary)


class Animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

A = Animals()
print(A.make_sound)

class Animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animals):
    def __init__(self, name, breed):
        Animals.__init__(self, name, species='Dog')
        self.breed = breed

    def make_sound(self):
        print('Bark!')

class Cat(Animals):
    def __init__(self, name, breed):
        Animals.__init__(self, name, species='Cat')
        self.breed = breed
    
    def make_sound(self):
        print('Meow!')

A = Animals('Dog', 'Dog')
A.make_sound()
D = Dog('Dog', 'Doberman')
D.make_sound()
C = Cat('Cat', 'Persian')
C.make_sound()
