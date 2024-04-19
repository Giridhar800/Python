stack = []
while True:
    print('1.Push')
    print('2.Pop')
    print('3.View')
    print('4.Exit')

    opt = int(input("enter option=>"))
    if opt == 1:
        e = int(input("enter pushing element"))
        stack.append(e)
        print(f"{e} : pushed in stack")

    elif opt == 2:
        if len(stack) == 0:
            print("stack is empty")
        else:
            e = stack.pop()
            print(f"element poped {e} ")
    elif opt == 3:
        print(stack)
    elif opt == 4:
        break
            
