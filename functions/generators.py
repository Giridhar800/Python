import random
def random_generator(start,stop,count):
    for i in range(count):
        m=random.randint(start,stop)
        yeild m

def main():
    rg = random_generator(5,10,3)
    n1 = next(rg)
    print(n1)
    n2 = next(rg)
    print(n2)
    n3 = next(rg)
    print(n3)


main()
