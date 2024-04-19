import threading
# import pdb;

class Bus:
    
    def __init__(self):
        self.seats = 40
        self.l = threading.Lock()
    def reserve(self,name,n):
        self.l.acquire()
        for i in range(n):
            self.seats = self.seats - 1
        print(f" {name} your seats reserved")
        print(f" available seets{self.seats}")
        self.l.release()

class Reservedthread(threading.Thread):
    def __init__(self,b,name,n):
        super().__init__()
        self.bus = b
        self.name = name
        self.n = n
    def run(self):
        self.bus.reserve(self.name,self.n)

def main():
    bus1 = Bus()
    t1 = Reservedthread(bus1,"giri",5)
    t2 = Reservedthread(bus1,"sycho",2)
    t3 = Reservedthread(bus1,"venkey",10)
    t1.start()
    t2.start()
    t3.start()

main()
    
