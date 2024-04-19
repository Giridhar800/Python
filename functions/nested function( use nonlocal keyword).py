def fun1():
    x = 100
    x = 300 # dammy
    def fun2():
        nonlocal x
        x = 200
        print(x)
    fun2()
    print(x)
    # print(__doc__)
    

def main():
    fun1()

main()
