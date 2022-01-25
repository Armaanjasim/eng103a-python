print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


# A1a:
def integer_divisor(num1=0):
    if num1 == 0:
        num1 = input("Write a number that you want to know the divisors of: ")
    new_list = []
    if num1.isdigit():
        num1 = int(num1)
        for i in range(1, int(num1) + 1):
            if (num1 % i) == 0:
                new_list.append(i)
    else:
        print("Select a number please!")
        integer_divisor()
    return new_list


# print(integer_divisor())

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


# A1b:
def factor_of_two_numbers():
    factor2_is_correct = True
    factor1 = input("Pick the first number: ")
    if factor1.isdigit():
        while factor2_is_correct:
            factor2 = input("Pick the second number: ")
            if factor2.isdigit():
                factor2_is_correct = False
            else:
                print("Enter a digit for the second number please!")
    else:
        print("Enter a digit for the first number please!")
        factor_of_two_numbers()

    if int(factor1) == int(factor2):
        print(True)
        print("Factor == Factor")
    elif int(factor1) > int(factor2):
        list_factor = integer_divisor(factor1)
        if int(factor2) in list_factor:
            print(True)
        else:
            print(False)
    elif int(factor1) < int(factor2):
        list_factor = integer_divisor(factor2)
        if int(factor1) in list_factor:
            print(True)
        else:
            print(False)


# factor_of_two_numbers()


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:
def string_into_alphabet(string_letter=False):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    index = 0
    skip_this_part = True
    if not string_letter:
        string_letter = input("Please type a letter to know what place it is in the alphabet: ")
    else:
        skip_this_part = False
    if string_letter.isalpha():
        if len(string_letter) == 1:
            index = alphabet.index(string_letter.lower()) + 1
            if skip_this_part:
                print(index)
        else:
            print("Please enter 1 character only!")
            string_into_alphabet()
    else:
        print("Please enter an alphabet character only!")
        string_into_alphabet()
    return index


# string_into_alphabet()


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


# A2b:
def persons_name_into_id():
    alphabet = ["123", "456", "789", "101", "112", "131", "415", "161", "718", "192", "021", "222", "324",
                "252", "627", "282", "930", "313", "233", "343", "536", "373", "839", "404", "142", "434"]
    string_name = input("Please enter your name to convert into an id: ")
    code_name = ""
    if string_name.isalpha():
        for char in string_name:
            x = string_into_alphabet(char)
            # print(alphabet[x])
            code_name += alphabet[x-1]
    else:
        print("Silly your name can't have a number or space. Enter an alphabet character only!")
        persons_name_into_id()
    print(f"Your code name is: {code_name}")
    return code_name


# persons_name_into_id()

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


# A2c:
def turn_id_into_password():
    name_id = persons_name_into_id()
    for number in name_id:
        name_id = int(name_id) - int(number)
    print(f"Password is: {name_id}")


# turn_id_into_password()




# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.


# A3a:
def check_prime_number():
    number = input_number("What number would you like to check is a prime number? ")
    ans = "Prime"
    if number:
        for i in range(2, int(number)):
            if int(number) % i == 0:
                ans = "Not Prime"
                break
    else:
        print("You need a digit please!")
        check_prime_number()
    print(ans)

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


# A3b:
def input_number(question):
    ans = input(question)
    if ans.isdigit():
        return ans
    else:
        return False


check_prime_number()

# -------------------------------------------------------------------------------------- #
