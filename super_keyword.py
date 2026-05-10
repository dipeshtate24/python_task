class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang


e1 = Employee("Suresh patil", "id_1")
e2 = Programmer("Sachin Mishra", "id_2", "C++")
print(e1.name)
print(e2.name)
print(e2.id)
print(e2.lang)
