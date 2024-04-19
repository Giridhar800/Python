class Student:
    def __init__(self):
        self.__rollno = None
        self.__name = None
        self.__course = None
    def read_student(self):
        self.__rollno = int(input("enter rollno"))
        self.__name = input("enteer name")
        self.__course = input("enter course")
    def print_student(self):
        print(f' Rollno :{self.__rollno}')
        print(f' Name :{self.__name}')
        print(f' Course :{self.__course}')
def main():
    s1=Student()
    s1.read_student()
    s1.print_student()
    

main()
