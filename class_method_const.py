class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

e = Employee('kumar', 20000)
e.name = 'Kumar'
e.salary = 2000
print(e.name)
print(e.salary)


string = "Kumar-20000"
e = Employee.fromstr(string)
e = Employee(string.split("-")[0], string.split("-")[1])
print(e.name)
print(e.salary)

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
string = "Akshya,35"
p = Person.from_string(string)
print(p.name)
print(p.age)
