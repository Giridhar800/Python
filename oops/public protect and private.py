class A:
    def __init__(self):
        self.x = 100
        self._y = 200
        self.__z = 300

class B(A):
    def __init__(self):
        super().__init__()
    def m1(self):
        print(f" Public x={self.x}")
        print(f" Protect y={self._y}")
       # print(f" Private y={self.__z}")
        
def main():
    o1 = B()
    o1.m1()
    print(o1.x)

main()
