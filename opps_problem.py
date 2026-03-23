# class C2dvec:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return f"{self.icap + self.jcap}"

# class C3dvec(C2dvec):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.kcap = k
    
#     def __str__(self):
#         return f"{self.icap + self.jcap + self.kcap}"


# v2d = C2dvec(1, 3)
# v3d = C3dvec(1, 9, 7)
# print(v2d)
# print(v3d)


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