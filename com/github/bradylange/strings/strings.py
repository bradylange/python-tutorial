# Developer: Brady Lange
# Date: 07/28/2019
# Description:

# One line comment style
'''
Multi-line comment style
'''

strOne = "String's"
# Escape single quote
strTwo = 'String\'s'
strTwo = r'String\'s'
# Escape back slash
strThr = "String\\'s"
strSpc = "      String with extra space      "
print(strOne)
print(strTwo)
print(strThr)

# Convert string to lowercase letters
print(strOne.lower())
print(strOne.count("i"))

# Print single character in string
print(strOne[4])
print(strOne[2:4])

# Strip white space from string
print(strSpc.strip())

print(strOne.replace("i", "a"))

print(strOne.islower())

print(strThr.split("\\"))

# Print string 100 times
print(strOne * 100)