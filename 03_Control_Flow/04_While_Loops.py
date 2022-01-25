# WHILE LOOPS

# i = 1
#
# while i <= 10:
#     print(i)
#     i += 1

prompt_user = True
age = None
while prompt_user:
    age = input("What is your age?\n")
    if age.isdigit() and 0 < int(age) < 120:
        prompt_user = False
    else:
        print("Please provide age in digits")

print(f"Double your age is {int(age) * 2}")
