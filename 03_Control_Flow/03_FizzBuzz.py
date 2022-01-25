# Basic Version

#  While True Loop For Starting Number
while True:
    startNum = input("Pick a starting number for fizzbuzz 1-10000: ")
    if startNum.isdigit() and 0 < int(startNum) < 10000:
        # Check if the input is a number and greater than 0
        break
        # If the input meets the requirements it breaks from the while loop
    else:
        print("Pick an 'Integer' between '1-10000'")
        # If the input doesn't meet the requirements it prints the statement and then loops till it does

#  While True Loop For Ending Number
while True:
    endNum = input("Pick an ending number for fizzbuzz 1-10000: ")
    if endNum.isdigit() and 0 < int(endNum) < 10000:
        # Check if the input is a number and greater than 0
        break
        # If the input meets the requirements it breaks from the while loop
    else:
        print("Pick an 'Integer' between '1-10000'")
        # If the input doesn't meet the requirements it prints the statement and then loops till it does

#  While True Loop For First Word
while True:
    word1 = input("Input first keyword for numbers divisible by 3 (Only alphabetical characters & No Spaces): ")
    if word1.isalpha():
        # Check if the input is a number and greater than 0
        break
        # If the input meets the requirements it breaks from the while loop
    else:
        print("You must only select alphabetical characters 'a', 'A', 'b', 'B' etc")
        # If the input doesn't meet the requirements it prints the statement and then loops till it does

#  While True Loop For Second Word
while True:
    word2 = input("Input first keyword for numbers divisible by 5 (Only alphabetical characters & No Spaces): ")
    if word2.isalpha():
        # Check if the input is a number and greater than 0
        break
        # If the input meets the requirements it breaks from the while loop
    else:
        print("You must only select alphabetical characters 'a', 'A', 'b', 'B' etc")
        # If the input doesn't meet the requirements it prints the statement and then loops till it does


counter1 = 0
counter2 = 0
counter3 = 0

fizz = 3
buzz = 5

for i in range(int(startNum), int(endNum)+1):
    if i % fizz == 0 and i % buzz == 0:  # Checks if the number is divisible by 3 and 5
        print(word1 + word2)
        counter3 += 1  # Counter for how many times it has run through this if statemen
    elif i % fizz == 0:  # Checks if the number is divisible by 3
        print(word1)
        counter1 += 1  # Counter for how many times it has run through this if statemen
    elif i % buzz == 0:  # Checks if the number is divisible by 5
        print(word2)
        counter2 += 1  # Counter for how many times it has run through this if statement
    else:
        print(i)  # Prints the number if it is not divisible by 3 or 5

print(f"\nThe number of {word1 + word2} that has appeared is {counter3} ")
print(f"The number of times {word1} has appeared by itself is: {counter1} ")
print(f"The number of {word2} has appeared by itself is: {counter2} ")
