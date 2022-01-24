age = 50

if 18 <= age <= 50:
    print("You are allowed to buy a ticket for this film.")
    print("Enjoy the film!")
elif age > 50:
    print("Should you really be in the cinema")
elif age < 18:
    print("You are too young to watch this")
else:
    print("No Film Showing")

print("This will always print")


certificate = '15'

if certificate == 'U':
    print('Suitable for all ages')
elif certificate == 'PG':
    print('Parental Guidance Recommended')
elif certificate.upper() in ('12', '12A'):
    print('12 and above')
elif certificate == '15':
    print('15 and above')
