def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error! Dividing by zero is not allowed.")
        return None
    return a / b

def get_operator_function(operator):
    if operator == '+':
        return add
    elif operator == '-':
        return subtract
    elif operator == '*':
        return multiply
    elif operator == '/':
        return divide
    else:
        print("Error! Invalid operator.")
        return None
a = int(input("Enter first number: "))
while True:
   

    operator = input("Enter an operator (+, -, *, /): ")

    b = int(input("Enter second number: "))

    operator_function = get_operator_function(operator)

    if operator_function is not None:
        result = operator_function(a, b)
        if result is not None:
            print("The result is: ", result)

    choice = input("Do you want to continue (y/n)? ")

    if choice == 'n':
        break

    a = result