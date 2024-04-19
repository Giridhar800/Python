import socket
def main():
    s=socket.socket()
    s.bind(("localhost",30))
    s.listen(5)
    print("server is running....")
    c=s.accept()
    print("connectiion is established")

main()
