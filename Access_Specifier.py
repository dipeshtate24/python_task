

class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.age = age


# a = Employee()
a = Employee('Hemant', 32)
# print(a.__name) # cannot be access directly
print(a._Employee__name)
print(a.age)
print(a.__dir__())

class Student:
    def __init__(self):
        self._name = 'Shushant'
    
    def _funName(self): # Protected Method
        return 'CodeWithHarry'
    
class Subject(Student): # inheritance method
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())
