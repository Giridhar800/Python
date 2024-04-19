import threading

def even(start,stop):
    for num in range(start,stop):
        if num%2 == 0:
            print(f" even:{num}")
def odd(start,stop):
    for num in range(start,stop):
        if num%2 != 0:
            print(f" odd no:{num}")

def main():
    t1 = threading.Thread(target = even,args = (1,21))
    t2 = threading.Thread(target = odd,args = (1,21))
    t1.start()
    t2.start()
    

main()
    
