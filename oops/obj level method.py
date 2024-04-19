class Employee():
    def set_emp(self):
        self.empno=101
        self.empname="giri"
    def print_emp(self):
        print(self.empno,self.empname)
def main():
    emp1=Employee()
    emp1.set_emp()
    emp1.print_emp()
main()
    
