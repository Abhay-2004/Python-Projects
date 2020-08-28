#defining functions:
def addition(num1,num2):
    return num1 + num2
def subtraction(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("zero division error")

print("Select the operation: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division")

#input
operation = int(input("Enter Here: "))

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if operation == 1:
    print(num1, "+", num2, "=", addition(num1,num2))

eLif operation == 2:
    print(num1, "-", num2, "=", subtraction(num1,num2))

elif operation == 3:
    print(num1, "*", num2, "=", multiply(num1,num2))

elif operation == 4:
    print(num1, "/", num2, "=", divide(num1,num2))
