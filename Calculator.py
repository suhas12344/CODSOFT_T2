import math

num1 = float(input("Enter the first number: "))
operation = input("Enter an operation (+, -, *, /, sqrt): ")

if operation == 'sqrt':
    result = math.sqrt(num1)
else:
    num2 = float(input("Enter the second number: "))
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation!"

print("The result is:", result)
