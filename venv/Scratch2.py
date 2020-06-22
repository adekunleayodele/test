# num1 = float(input("Enter first number: "))
# oper = input("Enter operation: ")
# num2 = float(input("Enter second number: "))
inport pexpert
num1 = input("Enter first number: ")
oper = input("Enter operation: ")
num2 = input("Enter second number: ")

import re
import pexpect


if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    ans = str(num1) + str(num2)
    print(ans)
elif oper == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
