def dfun(f):  # decorator part
    def nfun():
        f()
        print("New features")
    return nfun


@dfun
def fun1():
    print("inside function1")

@dfun
def fun2():
    print("inside function2")

def main():
    fun1()
    fun2()
main()
