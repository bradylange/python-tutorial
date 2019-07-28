# Developer: Brady Lange
# Date: 06/30/2019
# Description: Python printing.

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