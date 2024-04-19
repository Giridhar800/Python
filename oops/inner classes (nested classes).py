class A: # outer class
    class B: # inner class
        def m1(self):
            print("m1 of b class")

    def m2(self):
        print("m2 of A class")

def main():
    o1 = A.B()
    o1.m1()
    o2 = A()
    o2.m2()

main()
