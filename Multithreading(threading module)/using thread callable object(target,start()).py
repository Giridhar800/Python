import threading

def even():
    for num in range(1,21):
        if num%2 == 0:
            print(f"Even no:{num}")

def odd():
    for num in range(1,21):
        if num%2 != 0:
            print(f" odd num:{num}")
def main():
    t1 = threading.Thread(target = even)
    t2 = threading.Thread(target = odd)
    t1.start()
    t2.start()

main()
