class A:
    def __m1(self):
        print("private m1 member")
    
    def m2(self):
        print("m2 is public method")
      
def main():
    o1 = A()
    
    o1.m2()

main()
