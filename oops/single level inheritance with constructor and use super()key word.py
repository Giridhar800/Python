class A:
    def __init__(self):
        self.x = 100

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 200

def main():
    o1 = B()
    print(o1.y)
    print(o1.x)

main()
