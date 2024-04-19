class A:
    def m1(self):
        print("m1 of A class")

class B(A):
    def m2(self):
        print("m2 of B class")

def main():
    o1 = B()
    o1.m1()
    o1.m2()

main()
