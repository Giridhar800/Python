cart = {}
while True:
    print("1.Add Product")
    print("2.Update Product")
    print("3.Delete product")
    print("4.Search")
    print("5.View Cart")
    print("6.Exit")

    opt = int(input("enter your option=>"))

    if opt == 1:
        pname = input("product name")
        if pname in cart:
            print(pname,"exist in cart")
        else:
            qty =int(input("enter qty:"))
            cart[pname] = qty
            print("product added...")

    elif opt == 2:
        pname = input("product name")
        if pname in cart:
            qty = int(input("enter qty"))
            cart[pname] = qty
            print("qty updated...")
        else:
            print(pname, "not exists in the cart")


    elif opt == 3:
        pname = input("enter product name")
        if pname in cart:
            del cart[pname]
            print("product deleted from the cart sucussfully...")
        else:
            print(pname,"not exists in the cart")

    elif opt == 4:
        pname =input("enter product name")
        if pname in cart:
            qty = cart[pname]
            print("QTY is",qty)
        else:
            print("product not exist")

    elif opt == 5:
        for pname,qty in cart.items():
            print(pname,qty)

    elif opt == 6:
        break
        
