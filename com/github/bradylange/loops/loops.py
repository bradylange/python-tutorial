# Developer: Brady Lange
# Date: 07/28/2019
# Description:

i = 0
# Loop until condition is met
while i < 22:
    # Print value
    print("Value:", i)
    # Increment by 1
    i += 1

sum = 0
end = False
while end is not True:
    num = float(input("Enter a number to be summed: "))
    sum += num
    print(sum)
    end = input("Enter 'True' if you want to stop and 'False' if not: ").lower().capitalize()