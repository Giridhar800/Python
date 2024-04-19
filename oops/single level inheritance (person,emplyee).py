class Person:
    def __init__(self):
        self.__name = None
    def setname(self,n):
        self.__name = n
    def getname(self):
        return self.__name

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.__job = None
    def setjob(self,j):
        self.__job = j
    def getjob(self):
        return self.__job

def main():
    e1 = Employee()
    e1.setname("Giri")
    e1.setjob("Developer")
    print(f'''Name:{e1.getname()}
jobis:{e1.getjob()}''')

main()
        
