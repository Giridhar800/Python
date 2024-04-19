for r in range(1,6):
    for c in range(1,6):
        if c>=r:
            print(c,end=" ")
        else:
            print(" ", end=" ")
    print()
