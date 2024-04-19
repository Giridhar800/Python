import mysql.connector as m
def main():
    cn = m.connect(database = 'sychoyadav',user = 'root',password = 'giri')
    c = cn.cursor()
    while True:
        r = int(input("enter rollno"))
        n = input("enter name")
        f = float(input("enter fees"))
        c.execute("insert into student values(%s,%s,%s)",params = [r,n,f])
        print(c.rowcount)

        ans = input("Add another student:")
        if ans == "no":
            cn.commit()
            cn.close()
            break

main()
