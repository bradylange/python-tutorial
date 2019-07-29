# Developer: Brady Lange
# Date: 07/28/2019
# Description: Logic and logical operations.

true = True
false = False

print(true == false)
print(true is false)

numOne = 1
numTwo = 1000

strOne = "Brady"
strTwo = "Lange"

numOne > numTwo
numOne < numTwo
numOne >= numTwo
numOne <= numTwo
numOne == numTwo
numOne != numTwo

print(strOne == strOne)
print(strOne is strOne)

print(strOne.isalpha() and strTwo.isalpha())
print(strOne.isalpha() or strTwo.isnumeric())
print(not numOne < numTwo)
print(strOne.isalpha() and not strTwo.isalpha())

# Conditional statements
if numOne == 0 and numTwo == 0:
    print(numOne, "and", numTwo, "are 0")
if numOne < numTwo:
    print(numOne, "is less than", numTwo)
else:
    print(numOne, "is greater than", numTwo)

color = input("What is your favorite color? ")
if color.lower() == "blue":
    print("Favorite color is:", color)
elif color.lower() == "red":
    print("Favorite color is:", color)
elif color.lower() == "green":
    print("Favorite color is:", color)
else:
    print("Color is not available.")

# Nested conditional statements
if numOne % 2 == 0:
    print(numOne, "is even")
    if numOne < 0:
        print(numOne, "is negative")
    else:
        print(numOne, "is positive")
else:
    print(numOne, "is not even")
    if numOne < 0:
        print(numOne, "is negative")
    else:
        print(numOne, "is positive")