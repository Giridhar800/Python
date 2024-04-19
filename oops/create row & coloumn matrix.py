class Matrix:
    def __init__(self):
        self.__l = []

    def read_matrix(self):
        r = int(input("enter how many rows"))
        c = int(input("enter how many coloumns"))
        for i in range(r):
            row = []
            for i in range(c):
                values = int(input("enter values"))
                row.append(values)
            self.__l.append(row)

    def print_matrix(self):
        for row in self.__l:
            for col in row:
                print(col,end = ' ')
            print()

def main():
    mat1 = Matrix()
    mat1.read_matrix()
    mat1.print_matrix()
main()
