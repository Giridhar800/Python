class Math:
    @staticmethod
    def factorial(num):
        f = 1
        for i in range(1,1+num):
            f = f*i
            return f

    @staticmethod
    def power(num,p):
        return num**p

def main():
    r1 = Math.factorial(5)
    r2 = Math.power(4,2)
    print(r1,r2)

main()
