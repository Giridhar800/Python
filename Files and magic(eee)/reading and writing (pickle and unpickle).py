import pickle

class Employee:
    empno = 101
    ename = "giri"
    salary = 10000

e1 = Employee()
f = open("emp.ser","wb")
pickle.dump(e1,f)
f.close()

f = open("emp.ser","rb")
emp1 = pickle.load(f)
print(emp1.empno,emp1.ename,emp1.salary)
