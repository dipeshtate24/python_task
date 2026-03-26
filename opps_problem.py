class C2dvec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap + self.jcap}"

class C3dvec(C2dvec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    
    def __str__(self):
        return f"{self.icap + self.jcap + self.kcap}"


v2d = C2dvec(1, 3)
v3d = C3dvec(1, 9, 7)
print(v2d)
print(v3d)


class Animals:
    Type = 'Mammal'

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Dog is brakking.")
    
d = Dog()
d.bark()

class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary

e = Employee()
print(e.increment)
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 2000
e.increment = 2
print(e.salaryAfterIncrement)

class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return Complex(self.real+c.real, self.imaginary+c.imaginary)
    
    def __mul__(self, c):
        mulReal = (self.real * c.real) - (self.imaginary * c.imaginary)
        # mulImg = (self.real * c.imaginary) - (self.imaginary * c.real)
        mulImg = (self.real * c.imaginary) + (self.imaginary * c.real)

        return Complex(mulReal, mulImg)
    
    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}"
        else:
            return f"{self.real} + {self.imaginary}i"

# c1 = Complex(8, 5)
# c2 = Complex(1, 4)
c1 = Complex(333, 2)
c2 = Complex(1, 37)
print(c1)
print(c2)
print(c1+c2)
print(c1*c2)


class Vector:
    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])

        return Vector(newlist)
    
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
        

v1 = Vector([1, 4, 6])
v2 = Vector([1, 6, 9])
print(v1)
print(v2)
print(v1 + v2)
print(v1 * v2)


import random 
randoNumber = random.randint(1, 100)

a = 1
for i in range(0, 5):
    userGuess = int(input("Enter your number:"))
    if a < 5:
        if userGuess == randoNumber:
            print("Your Guess Correct Number.")
            break
        else:
            print(f"{5-a} chances remain")
        a += 1
    else:
        print("No chance left try again.")
