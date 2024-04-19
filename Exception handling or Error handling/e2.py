def main():
    try:
        print(" inside try block")
        n1 = int(input("first num :")) # 4 6
        n2 = int(input("second num :"))# 2 0
        n3 = n1/n2 #4/2
        print(f'Result is {n3}')

    except ZeroDivisionError :
        print("inside except block")
        print(" cannot divided by zero")

    finally:
        print("inside block")
    print("continue....")

main()

    
