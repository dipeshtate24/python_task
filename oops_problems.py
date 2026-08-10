class Programmer:
    company = "Microsoft"

     
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of company is {self.company} programmer is {self.name} and current product is {self.product}.")

Person1 = Programmer("Kiran", 'Skype')
Person2 = Programmer("Alka", "Github")
Person1.getInfo()
Person2.getInfo()


class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number**2}")

    def squareroot(self):
        print(f"The value of {self.number} square root is {self.number**0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number**3}")

    @staticmethod
    def greet():
        print("*******Hello welcome to world best calculator.***********")
a = Calculator(3)
a.square()
a.squareroot()
a.cube()
a.greet()


class Sample:
    a = "Sam"

obj = Sample()
obj.a = 'Vikky'

print(Sample.a)
print(obj.a)


class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f"The name of the train is {self.name}")
        print(f"Total seat is available is {self.seats}")

    def fare_info(self):
        print(f"Total fare cost is {self.fare}")

    # def getSeat(self):
    #     print(f"Total seat is available is {self.seats}")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked!. Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print('Sorry, this train is full. Kindly book a Tatkal ticket.')

intercity = Train("Intercity Experess: 14015", 90, 300)
intercity.get_status()
intercity.fare_info()
intercity.bookTicket()
intercity.get_status()

