num = int(input("enter any number"))
num1 = num
s = 0

if num >= 100 and num <= 999:
    while num > 0:
        r = num%10
        s = s+r**3
        num = num //10
    if s == num1:
        print(num1,"is armstrong number")
    else:
        print(num1,"is not armstrong number")
else:
    print("input 3 digit number")
