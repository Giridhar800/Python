a,b,c = map(int,input("enter 3 values").split())

if a > b:
    if a > c:
        print(a,"is maximum")
    else:
        print(c,"is maximum")
elif b > c:
    print(b,"is maximum")
else:
    print(c,"is maximum")
