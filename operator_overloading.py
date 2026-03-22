class Number:
    def __init__(self, num):
          self.num = num
        
    def __add__(self, num2):
        print('Lets add')
        # return 300
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num
    
    def __str__(self):
        return f"Demical Number: {self.num}"    
    
    def  __len__(self):
        # return f"length of Number:{self.num}"
        return 1
    
# n1 = Number(4)
# n2 = Number(6)
# sum = n1 + n2
# mul = n1 * n2
# print(sum)
# print(mul)
n = Number(9)
print(n)
print(len(n))