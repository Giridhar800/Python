n = int(input("enter n value")) # without comprehension

stud_dict = {}
for i in range(n):
    rollno = int(input("enter rollno"))
    name = input("enter name")
    stud_dict[rollno] = name
print(stud_dict)

# with copmprehension

m = int(input("enter m value"))
sdict = {int(input("enter rollno")):input("enter name") for i in range(m)}
print(sdict)
