class Product:
    def __init__(self,pname,price):
        self.pname = pname
        self.price = price

def main():
    n = int(input("enter howmany products"))
    productlist = []
    for i in range(n):
        pname = input("enter product name")
        price = int(input("enter price"))
        p = Product(pname,price)
        productlist.append(p)
    for p in productlist:
        print(f"{p.pname}....>{p.price}")
main()
    
    
    
