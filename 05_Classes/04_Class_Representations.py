# class Location:
#     def __init__(self, lati, long):
#         self.lati = lati
#         self.long = long
#
#     def __repr__(self):
#         return f"Location: {self.lati}, {self.long}"
#
#     def __str__(self):
#         return f"{self.lati}, {self.long}"
#
#     def __format__(self, format_spec):
#         if format_spec == "latigs":
#             return f"A{self.lati}"
#         else:
#             return self.__str__()
#
# bham_academy = Location(232.322, 23231.3)
# print(repr(bham_academy))
# print(bham_academy)
