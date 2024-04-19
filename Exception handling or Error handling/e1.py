try:
    n1 = int(input("first num :")) # 4 6
    n2 = int(input("second num :"))# 2 0

    n3 = n1/n2 #4/2
    print(f'Result is {n3}')

except ZeroDivisionError :
    print("somthing by zero not excute")

except ValueError:
    print("only gives inteeger value")
    

    
# n1 = int(input("first num :")) # 4 6
# n2 = int(input("second num :"))# 2 0
# n3 = n1/n2 #4/2
# print(f'Result is {n3}')

    
