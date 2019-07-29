# Developer: Brady Lange
# Date: 07/28/2019
# Description: Python printing.

import math

x = 12
y = 8
name = "Brady"
age = 21

print("{0} + {1} = {2}".format(x, y, x + y))
print("Hello", "universe!", sep = "-----")
print("Hi %s, your age is %d." % (name, age))
print("Grade: %.2f" % 99.3)
userInp = input("How are you today? ")
print("User's input: '%s'" % userInp)

# Built-in functions
print(dir(__builtins__))
print(dir(math))
help(len)
print("My name is", len("Brady"), "characters long.")

firstNum = 2
secondNum = 5
sqrtNum = 100
print("{0}^{1} = {2}".format(firstNum, secondNum, pow(firstNum, secondNum)))
print("Square root of {0} is {1}".format(sqrtNum, math.sqrt(sqrtNum)))

print("\nEnter two numbers to see which is larger:")
firstNum = float(input("Enter the first number: "))
secondNum = float(input("Enter the second number: "))
print("The largest number is", max(firstNum, secondNum))