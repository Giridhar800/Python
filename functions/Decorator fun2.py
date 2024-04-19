def dfun(f):  # decorator part
    def smart_div(n1,n2):
        if n2 == 0:
            return 0
        else:
            return f(n1,n2)
    return smart_div

@dfun
def div(n1,n2):
    return n1/n2

def main():
    n1 = int(input("enter first number:"))
    n2 = int(input("enter second number:"))
    res = div(n1,n2)
    print(f" result is {res:.2f}")

main()
    
