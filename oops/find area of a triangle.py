class Triangle:
    def __init__(self):
        self.__base = 0.0
        self.__height = 0.0
        
    def set_base(self,b):
        self.__base = b
    def set_height(self,h):
        self.__height = h
        
    def find_area(self):
        area = self.__base*self.__height*0.5
        return area

def main():
    t1 = Triangle()
    t1.set_base(1.5)
    t1.set_height(1.7)
    a = t1.find_area()
    print(f"Area of a Triangle is {a:.2f}")

main()
