n = int(input("enter how many students"))

stud_dict = {}
for i in range(n):
    name = input("enter name:")
    marks = list(map(int,input("enter 2 sub marks").split()))
    if name not in stud_dict:
        stud_dict[name] = marks
    print(name,"is exist")

print(stud_dict)
