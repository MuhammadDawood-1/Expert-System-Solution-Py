print("------- Calculator -------")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

operator = input("Enter Operator (+, -, *, /): ")

if operator == "+":
    print("Answer =", num1 + num2)

elif operator == "-":
    print("Answer =", num1 - num2)

elif operator == "*":
    print("Answer =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Answer =", num1 / num2)
    else:
        print("Division by zero is not allowed!")

else:
    print("Invalid Operator!")