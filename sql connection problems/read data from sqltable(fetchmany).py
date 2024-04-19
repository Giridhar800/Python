import mysql.connector as m
def main():
    cn = m.connect(database = "sychoyadav",user = "root",password = "giri")
    c = cn.cursor()
    c.execute("select * from employee")

    rows = c.fetchmany(3)
    print(rows)
    rows = c.fetchmany(3)
    print(rows)
    rows = c.fetchmany(3)
    print(rows)
   
main()
