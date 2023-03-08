firstnumber = int(input("Input the first number: "))
secondnumber = int(input("Input the second number: "))
operatorselection = input("Select an operator, the options are: + - * / ")
theoperator = ""
def add(sum1,sum2):
    return(sum1 + sum2)

def subtract(subtract1,subtract2):
    return(subtract1 - subtract2)

def multiply(multiply1,multiply2):
    return(multiply1*multiply2)

def divide(divide1,divide2):
    return(divide1/divide2)


def calculator(num1,num2,operator):
    if operator == "+":
        total = add(num1,num2)
        theoperator = "Add"
        
    elif operator == "-":
        total = subtract(num1,num2)
        theoperator = "Substract"
        
    elif operator == "*":
        total = multiply(num1,num2)
        theoperator = "Multiply"
        
    elif operator == "/":
        total = divide(num1,num2)
        theoperator = "Divide"

    print("Results:", theoperator +"ing", num1, "by", num2, "=", total)
    
    
calculator(firstnumber,secondnumber,operatorselection)

