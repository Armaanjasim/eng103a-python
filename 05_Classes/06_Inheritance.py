# Inheritance & Polymorphism

class Mammal:
    def __init__(self, name):
        self.warm_blooded = True
        self.name = name

    def reproduce(self):
        print("Giving birth to live young")


class Horse(Mammal):
    def __int__(self, name):
        super().__init__(name)
        self.legs = 4


h = Mammal("Charlie")
s = Horse("Shadow")
print(h.name)
print(s.name)
s.reproduce()