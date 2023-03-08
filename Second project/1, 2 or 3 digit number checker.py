number = int(input("write a number "))

if number <= 9:
    print("Its one digit")
elif number <=99:
    print("its a 2 digit")
elif number <=999:
    print("Its a 3 digit number")
else:
    print("its bigger than a 3 digit number")