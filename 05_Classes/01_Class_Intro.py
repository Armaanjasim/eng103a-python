# OOP - Object-Oriented Programming
#
# class Dog:
#
#     animal_kind = "Canine"  # class variable
#
#     def bark(self):  # method
#         return "Woof!"
#
#
# fido = Dog()
# print(fido, type(fido))
# print(fido.animal_kind)
# print(fido.bark())


class Cat:
    def __init__(self, colour):
        self.cat_type = "Lion"
        self.colour = colour

    def roar(self):
        return "Roarr!"

    def loud_roar(self):
        return self.roar().upper()


Arslan = Cat("Blue")
print(Arslan.colour, Arslan.cat_type, Arslan.loud_roar())