class A:
    def __init__(self):
        self.__x = 100 # private
        self.y = 200   # public
    
def main():
    o1 = A()
    print(o1.y)
main()
