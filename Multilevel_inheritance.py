class Animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def showDetails(self):
        print(f"Name:{self.name}")
        print(f"Species:{self.species}")


class Dog(Animals):
    def __init__(self, name, breed):
        Animals.__init__(self, name, species='Dog')
        self.breed = breed

    def showDetails(self):
        Animals.showDetails(self)
        print(f"Breed: {self.breed}")


class Goldenreteriver(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed='Goldenreteriver')
        self.color = color

    def showDetails(self):
        Dog.showDetails(self)
        print(f"Color:{self.color}")

D = Goldenreteriver('tommy', 'golden')
D.showDetails()
print(Goldenreteriver.mro())
        