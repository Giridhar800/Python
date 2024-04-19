class A:
    def __init__(self):
        self.x = 100

class B:
    def __init__(self):
        self.y = 200

class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self) # very imp multiple inheritance
        self.z = 300

def main():
   o1 = C()
   print(f" x = {o1.x},y = {o1.y},z = {o1.z}")
main()


          
        
