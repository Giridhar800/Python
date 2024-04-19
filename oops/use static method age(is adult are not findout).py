class Person:
    def __init__(self,n,a):
        self.__name = n
        self.__age = a
        
    def print_person(self):
        print(f"Name:{self.__name}")
        print(f"Age:{self.__age}")

    def get_age(self):
        return self.__age

    @staticmethod
    def isAdult(age):
        if age>=18:
            print("Adult")
        else:
            print("is not adult")
def main():
    p1 = Person("Giri",25)
    p1.print_person()
    a = p1.get_age()
    Person.isAdult(a)

main()
