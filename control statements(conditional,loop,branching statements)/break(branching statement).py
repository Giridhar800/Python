num = 1
n = int(input("enter n values"))
c = 0
while True:
    if num%2 == 0:
        print(num)
        c = c+1
    num = num+1
    if c == n:
        break
