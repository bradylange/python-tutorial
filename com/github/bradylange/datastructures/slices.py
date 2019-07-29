# Developer: Brady Lange
# Date: 07/28/2019
# Description:

l = [0, 1, 2, 3, 4, 5]
t = (0, 1, 2)
s = "0123"

# Instantiate slice information
sli = slice(1, 3)
print(l[sli])
print(l[1:3])
print(l[2:])
print(l[:2])
print(l[:])
print(l[::2])
# Print list from second value from right
print(l[-2:])
# Print list in reverse
print(l[::-1])