# Check if the number is odd or even.
# A number is even if devision by 2 gives a remainder is 0
# If the remainder is 1, it is odd number

num = int(input("enter any number:"))
if num%2==0:
    print("{0} is even".format(num))
else:
    print("{0} is odd".format(num))
