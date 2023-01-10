#Calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
    print(f"The addition is {num1 + num2}")

elif op == "-":
    print(f"The subtraction is {num1 - num2}")

elif op == "*":
    print(f"The multiplication is {num1 * num2}")

elif op == "x":
    print(f"The multiplication is {num1 * num2}")

elif op == "/":
    print(f"The division is {num1/num2}")

elif op == "%":
    print(f"The percentage is {num1 * num2/100}")

else:
    print("Invalid Operator")

'''
A futuro deberás encontrar la forma de:
- Ad a return
- Save answears
- Ad a Try Catch
'''