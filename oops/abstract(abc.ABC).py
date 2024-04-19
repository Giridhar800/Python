import abc
class Shape(abc.ABC): # Abstract class (or) ADt
    def __init__(self):
        self._dim1 = None
        self._dim2 = None

    def readdim(self):
        self._dim1 = float(input("Dim1:"))
        self._dim2 = float(input("Dim2:"))

    @abc.abstractmethod
    def find_area(self):
        pass

class Triangle(Shape):
    def __init__(self):
        super().__init__()
    def find_area(self): #overriding method
        return self._dim1 * self._dim2 * 0.5

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
    def find_area(self): #overriding method
        return self._dim1 *self._dim2

def main():
    t1 = Triangle()
    r1 = Rectangle()
    t1.readdim()
    r1.readdim()
    a1 = t1.find_area()
    a2 = r1.find_area()
    print(f" Area of a triangle{a1:.2f}")
    print(f"Area of a rectangle{a2:.2f}")
main()
    

