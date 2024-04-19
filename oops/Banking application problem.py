class Account:
    def __init__(self,a,cn,bal):
        self.__accno = a
        self.__accname = cn
        self.__balance = bal

    def deposite(self,t):
        self.__balance = self.__balance + t
    def withdraw(self,t):
        if t>self.__balance:
            print("insuff balance")
        else:
            self.__balance = self.__balance - t

    def print_Account(self):
        print(f"Account number  : {self.__accno}")
        print(f"customer Name : {self.__accname}")
        print(f"Balance : {self.__balance}")

def main():
    acc1 = Account(100001,"Sycho",10000.0)
    acc1.print_Account()
    acc1.deposite(1000)
    acc1.print_Account()
    acc1.withdraw(10000)
    acc1.print_Account()

main()
    
    
