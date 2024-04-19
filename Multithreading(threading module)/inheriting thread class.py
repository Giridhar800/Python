import threading

class Alphathread(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        for n in range(65,91):
            print(f"{self.name} -->{n:c}")
        print()

def main():
    t1 = Alphathread()
    t2 = Alphathread()

    t1.name = "giri"
    t2.name = "sycho"

    t1.start()
    t2.start()
main()
