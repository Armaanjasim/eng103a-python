# With Functions Version

def main():  # Main function
    num1 = start_number()
    num2 = end_number()
    keyword1 = first_keyword()
    keyword2 = second_keyword()
    # Counters for how many times the keywords have appeared
    counter1 = 0
    counter2 = 0
    counter3 = 0
    fizz = 3
    buzz = 5

    for i in range(int(num1), int(num2)+1):
        if i % fizz == 0 and i % buzz == 0:  # Checks if the number is divisible by 3 and 5
            print(keyword1 + keyword2)
            counter3 += 1  # Counter for how many times it has run through this if statement
        elif i % fizz == 0:  # Checks if the number is divisible by 3
            print(keyword1)
            counter1 += 1  # Counter for how many times it has run through this if statement
        elif i % buzz == 0:  # Checks if the number is divisible by 5
            print(keyword2)
            counter2 += 1  # Counter for how many times it has run through this if statement
        else:
            print(i)  # Prints the number if it is not divisible by 3 or 5

    print(f"\nThe number of {keyword1 + keyword2} that has appeared is {counter3} ")
    print(f"The number of times {keyword1} has appeared by itself is: {counter1} ")
    print(f"The number of {keyword2} has appeared by itself is: {counter2} ")


def check_if_input_is_number(num1):
    """
    Checks to see if the input is a number
    """
    if num1.isdigit():
        return True
    else:
        return False


def check_if_input_is_alpha_only(text1):
    """
    Checks to see if the input is an alphabetical list of characters
    """
    if text1.isalpha():
        return True
    else:
        return False


def input_number_question(question):
    """
    Asks question to the user (Trying to be efficient)
    """
    number = input(question)
    if check_if_input_is_number(number):
        return number
    else:
        return False


def input_keyword_question(question):
    keyword = input(question)
    if check_if_input_is_alpha_only(keyword):  # Checks to see if there is a value for the keyword
        return keyword
    else:
        return False  # Returns false if the keyword isn't alphabetical


def start_number():
    number = input_number_question("Pick a starting number for fizzbuzz: ")
    if number:
        return number
    else:
        print("Please enter a digit!")
        start_number()


def end_number():
    number = input_number_question("Pick an ending number for fizzbuzz: ")
    if number:
        return number
    else:
        print("Please enter a digit!")
        end_number()


def first_keyword():
    keyword = input_keyword_question("Please enter the first keyword: ")
    if keyword:
        return keyword
    else:
        print("Please enter alphabetic characters only!")
        first_keyword()


def second_keyword():
    keyword = input_keyword_question("Please enter the second keyword: ")
    if keyword:
        return keyword
    else:
        print("Please enter alphabetic characters only!")
        second_keyword()


main()
