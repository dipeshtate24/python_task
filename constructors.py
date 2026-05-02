class Person:
    def __init__(self, name, occ):
        print('I am a person')
        self.name = name  
        self.occ = occ
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person('Divya','HR')
a.info()
b = Person('Shubham', 'Developer')
b.info()