class Animal:

    def __init__(self, hunger=50, thirst=50):
        self.hunger = hunger
        self.thirst = thirst

    def eat(self, hinger=50, thirst=50):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1


tiger = Animal()
panther = Animal()
print(tiger.hunger, end=", ")
print(tiger.thirst, end=", ")
print(panther.hunger, end=", ")
print(panther.thirst)
tiger.play()
panther.play()
print(tiger.hunger, end=", ")
print(tiger.thirst, end=", ")
print(panther.hunger, end=", ")
print(panther.thirst)
tiger.eat()
tiger.drink()
panther.eat()
panther.drink()
print(tiger.hunger, end=", ")
print(tiger.thirst, end=", ")
print(panther.hunger, end=", ")
print(panther.thirst)