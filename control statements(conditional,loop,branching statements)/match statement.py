num = int(input("enter any number"))
match(num):
    case 1:
        print("This is first case")
    case 2:
        print("This is second case")
    case 3:
        print("This is third case")
    case 4:
        print("This is fourth case")
    case _:
        print("invalid number")
