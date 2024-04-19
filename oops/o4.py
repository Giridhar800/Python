class B:
    def __init__(self,x,y):
        print("inside constructor")
        print(x,y)
def main():
    o1=B(10,20)
    o2=B(30,40)
main()
