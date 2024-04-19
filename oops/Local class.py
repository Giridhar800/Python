class A: # outer class
    def m1(self):
        print("inside m1 of A class")

        class B: # Local class
            def m2(self):
                print("inside m2 of B class")
        o1 = B()
        o1.m2()
def main():
    o2 = A()
    o2.m1()

main()
