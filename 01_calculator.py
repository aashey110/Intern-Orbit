print("Enter any two numbers: ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

choice = input("Enter the operation you want to perform: ")

if choice == "+":
    output = num1 + num2
    print(f"{num1} + {num2} = {output}")

if choice == "-":
    output = num1 - num2
    print(f"{num1} - {num2} = {output}")

if choice == "*":
    output = num1 * num2
    print(f"{num1} * {num2} = {output}")

if choice == "/":
    output = num1 / num2
    print(f"{num1} / {num2} = {output}")

if choice != "+" and choice != "-" and choice != "*" and choice != "/":
    print("Invalid choice. Please enter a valid operation.")

