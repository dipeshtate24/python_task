# class Number:
#     def sum(self):
#         return self.a + self.b
    
# num = Number()
# num.a = 12
# num.b = 34
# s = num.sum()
# print(s)

"""
PascaleCase
EmpolyeeName

camelCase
isNumeric, isFloat

"""
class RailwayForm:
    fromType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

Application = RailwayForm()
Application.name = "Soham"
Application.train = "Rajdhani Express"

Application.printData()