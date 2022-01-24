# Lists (MUTABLE)

# shopping_list = ["eggs", "bread", "bananas", "tea"]
# print(shopping_list, type(shopping_list))
# print(len(shopping_list))
# print(shopping_list[0])
# print(shopping_list[-1])
#
# shopping_list[2] = "milk"
# print(shopping_list)
#
# shopping_list.append("biscuits")
# print(shopping_list)
#
# shopping_list.append("bread")
# print(shopping_list)
# shopping_list.remove("bread")
# print(shopping_list)
#
# shopping_list.pop(-1)

# mixed = [1, 2, "three", True, None, ["Another", "List"]]
# print(mixed)
#
# # print(mixed[::3])
#
# sublist = mixed[5]
# print(sublist)
# mixed[5][1] = "b"
# print(mixed)
# print(sublist)


# Tuples (IMMUTABLE)

colours = ("Red", "blue", "Green")
print(colours, type(colours))

list_in_tuple = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

print(len(list_in_tuple))
list_in_tuple[0][-1] = "SUCCESS"
print(list_in_tuple)
list_in_tuple[0].append("SUCCESS")
print(list_in_tuple)
