print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]


# A1a:
new_list = []
for i in range(0, 5):
    new_list.append(x[i])

print(new_list)

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]


# A1b:
multiple_of_2 = 2
new_list = []
for i in x:
    if i % multiple_of_2 == 0:
        new_list.append(i)

print(new_list)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]


# A1c:
new_list = []
for i in range(0, 6):
    if i % multiple_of_2 == 0:
        new_list.append(i)

print(new_list)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]


# A2a:
new_list = []
for i in names:
    new_list.append(i[0])

print(new_list)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]


# A2b:
new_list = []
for i in names:
    new_list.append(i.index(" "))

print(new_list)


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]


# A2c:
new_list = []
for i in names:
    new_list.append({i[0]: i[int(i.index(" "))+1]})

print(new_list)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
for i in list_of_lists:
    temp_set = set(i)
    if len(temp_set) == len(i):
        print(i)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered


# A4a:
number_entered_is_correct = True
while number_entered_is_correct:
    num1 = input("Choose a number greater than 100: ")
    if num1.isdigit():
        if int(num1) > 100:
            print(num1)
            number_entered_is_correct = False
        else:
            print("Pick a number greater than 100 only please!")
            continue
    else:
        print("Enter Numbers only Please!")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise


# A4b:
num1 = int(num1)
ans = "Prime"
for i in range(2, num1):
    if num1 % i == 0:
        ans = "Not Prime"
        break
print(ans)
