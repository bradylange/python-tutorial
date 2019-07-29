# Developer: Brady Lange
# Date: 07/28/2019
# Description:

# Lists
print("Lists:")
# List of numbers
l = [1, 6, 24, 5]
print(l)
# Index list
print(l[3])
print(len(l))

# Insert number into list
l.insert(0, 22)
print(l)

# Remove number '1' from list
l.remove(1)
print(l)

# Remove last value in list
l.pop()
print(l)

print(l.sort())
print(l.reverse())

# Append number '4' to list
l.append(4)

# Instantiate new list from old list
newL = l.copy()
print(newL.count(22))

# Clear entire list
l.clear()
# Delete entire list
del(l)

# Mixed data type list
lMix = ["Brady", 5, True]
print(lMix)
print(len(lMix))

# Tuples
print("\nTuples:")
# Instantiate tuple of numbers
t = (1, 2, 3, 4, 5, 6)
print(t)
print(t[2])
print(t.count(1))

# Concatenate tuples together
newT = t + t
print(newT)

# Print tuple five times
print(t * 5)

# Mixed data type tuple
tMix = ("Brady", 5, True)

# Sets
print("\nSets:")
# Instantiate set of numbers, only allows unique values
s = {1, 3, 3, 5, 7, 9}
print(s)
print(len(s))
# Add non-unique value
s.add(3)
print(s)
# Add multiple values
s.update([3, 3, 3, 22, 24])
print(s)
# Remove value
s.remove(3)
print(s)
# Remove value that is not there
s.discard(259)
print(s)
# Remove random value
s.pop()
print(s)
# Clear entire set
s.clear()
# Delete entire set
del(s)

# Instantiate set with constructor
sports = set(["Football", "Basketball"])
print(sports)

# Instantiate sets of numbers
setOne = {1, 2, 3}
setTwo = {3, 4, 1}

# Union
print(setOne | setTwo)
print(setOne.union(setTwo))
# Intersection
print(setOne & setTwo)
print(setOne.intersection(setTwo))
# Difference
print(setOne - setTwo)
print(setOne.difference(setTwo))
# Symmetric difference
print(setOne ^ setTwo)
print(setOne.symmetric_difference(setTwo))

# Dictionaries
print("Dictionaries:")
# Instantiate dictionary
dic = {"name": "Brady", "sport": "Football"}
print(dic)
print(dic["name"])
print(dic.get("name"))
dic["age"] = 21
print(dic)
print(len(dic))
dic.pop("age")
print(dic)
dic["sport"] = "Basketball"
dic.update({"sport": "Basketball"})
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
# Remove last item modified
dic.popitem()
print(dic)
# Clear entire dictionary
dic.clear()
# Delete entire dictionary
del(dic)

# Mixed data type key/pair dictionary
dicMixKey = {22: 22, True: True, (False, False): False}