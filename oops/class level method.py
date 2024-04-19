class A:
    def m1(self):
        print("this is object level method")

    @classmethod
    def m2(cls):
        print("This is class level method")

A.m2()
o1 = A()
o1.m1()
