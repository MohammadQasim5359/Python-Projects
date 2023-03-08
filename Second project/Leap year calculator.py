inputedyear = int(input("Input a year: "))

if inputedyear % 4 == 0:
    if inputedyear % 100 == 0 and inputedyear % 400 == 0:
        print("It's a leap year")
    elif inputedyear % 100 != 0:
        print("It's a leap year")
    else:
        print("It's not a leap year") 
else:
    print("It's not a leap year")
        

    