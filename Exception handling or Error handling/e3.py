def multiply(n1,n2):
    if n1==0 or n2==0:
        raise ValueError()
    else:
        return n1*n2
def main():
    try:
        res = multiply(2,2)
        print(res)
    except ValueError:
        print("cannot multiply number with zero")
main()
