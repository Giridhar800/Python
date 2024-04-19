import mysql.connector as m
def main():
    cn = m.connect(database = "sychoyadav",user = "root",password = "giri")
    c = cn.cursor()
    c.execute("select * from employee")

    #r1 = c.fetchone()
    #print(r1)
    #r2 = c.fetchone()
    #print(r2)

    while True:
        r = c.fetchone()
        if r == None:
            break
        print(r)
        
main()
