class A:
    def m1(self):
        print("m1 of A")
    def m2(self):
        print("m2 of A")

class B(A):
    def m3(self):
        print("m3 of B")
    def m1(self):
        print(" method overriding")
def main():
    o1 = B()
    o1.m1()
    o1.m2()
    o1.m3()

main()
        
