number1 = int(input("first number "))
number2 = int(input("second number "))
number3 = int(input("third number "))

if number1 <= number2 and number1 < number3 and number2 < number3:
    print(number1, number2, number3)
elif number1 <= number2 and number1 < number3 and number3 < number2:
    print(number1, number3, number2 )
elif number2 <= number1 and number2 < number3 and number1 < number3:
    print(number2, number1, number3 )
elif number2 <= number1 and number2 < number3 and number3 < number1:
    print(number2, number3, number1 )
elif number3 <= number1 and number3 < number2 and number1 < number2:
    print(number3, number1, number2 )
else:
    print(number3, number2, number1)
