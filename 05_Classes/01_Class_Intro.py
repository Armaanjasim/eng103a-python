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
    animal_kind = "Lion"

    def roar(self):
        return "Roarr!"

    def loud_roar(self):
        return self.roar().upper()


Arslan = Cat()
print(Arslan.loud_roar())