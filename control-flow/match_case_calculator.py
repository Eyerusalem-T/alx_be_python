number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    print( number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    if number2 == 0:
        print("Cannot divide by zero.")
    else:
        print(number1 / number2)
else:
    print("please enter a number")
