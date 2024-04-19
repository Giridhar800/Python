def calculater(n1,n2,a):
    res = a(n1,n2)
    return res

def main():
    res1 = calculater(10,5,lambda x,y:x+y)
    res2 = calculater(10,5,lambda x,y:x-y)
    print(f" Result 1 is {res1}")
    print(f" Result 2 is {res2}")

main()
