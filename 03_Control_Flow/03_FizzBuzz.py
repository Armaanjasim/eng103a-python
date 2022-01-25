# Basic Version

while True:
    startNum = input("Pick a starting number for fizzbuzz: ")
    if startNum.isdigit() and int(startNum) > 0 and int(startNum) > 0:
        # Check if the input is a number and greater than 0
        break
        # If the input meets the requirements it breaks from the while loop
    else:
        print("Pick an integer please")
        # If the input doesn't meet the requirements it prints the statement and then loops till it does

while True:
    endNum = input("Pick an ending number for fizzbuzz: ")
    if endNum.isdigit() and int(endNum) > 0:
        # Check if the input is a number and greater than 0
        break
        # If the input meets the requirements it breaks from the while loop
    else:
        print("Pick an integer please")
        # If the input doesn't meet the requirements it prints the statement and then loops till it does

word1 = input("Input first keyword for numbers divisible by 3: ")  # Could use isalpha() to check input
word2 = input("Input second keyword for numbers divisible by 5: ")  # Could use isalpha() to check input

for i in range(int(startNum), int(endNum)+1):
    if i % 3 == 0 and i % 5 == 0:  # Checks if the number is divisible by 3 and 5
        print(word1 + word2)
    elif i % 3 == 0:  # Checks if the number is divisible by 3
        print(word1)
    elif i % 5 == 0:  # Checks if the number is divisible by 5
        print(word2)
    else:
        print(i)  # Prints the number if it is not divisible by 3 or 5
