class Complex:
    def __init__(self):
        self.__real = 0.0
        self.__image = 0.0
    def set__real(self,r):
        self.__real = r
    def set__image(self,i):
        self.__image = i
    def get__real(self):
        return self.__real
    def get__image(self):
        return self.__image

def main():
    c1 = Complex()
    c1.set__real(1.5)
    c1.set__image(2.5)
    print(c1.get__real(),c1.get__image())
    # c1.set__real(3.5)
    # print(c1.get__real(),c1.get__image())
main()
    
