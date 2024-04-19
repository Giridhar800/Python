class Person:
    def __init__(self,n):
        self.__name = n
    def getname(self):
        return self.__name

class Employee(Person):
    def __init__(self,n,j):
        super().__init__(n)
        self.__job = j
    def getjob(self):
        return self.__job

class Salaryedemp(Employee):
    def __init__(self,n,j,s):
        super().__init__(n,j)
        self.__salary = s
    def getsalary(self):
        return self.__salary

def main():
    print(Salaryedemp.__mro__)
    e1 = Salaryedemp("Giri","Developer",50000)
    print(f"""name:{e1.getname()}
job:{e1.getjob()}
salary:{e1.getsalary()}""")

main()        
