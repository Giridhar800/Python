import threading

def main():
    t1 = threading.current_thread()
    print(t1.name)

main()
