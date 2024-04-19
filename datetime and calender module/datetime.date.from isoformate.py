import datetime as d

student_dict = {}
n = int(input("enter how many students"))

for i in range(n):
    rno = int(input("enter roll number"))
    name = input("enter name")
    course  = input("enter course")
    doj = d.date.fromisoformat(input("date of joining yyyy-mm-dd"))
    student_dict[rno] = [name,course,doj]
print(student_dict)
