import mysql.connector as m
def main():
    cn = m.connect(database = "sychoyadav",user = "root",password = "giri")
    c = cn.cursor()
    c.execute("select * from employee")

    rows = c.fetchall()
    print(rows)
    total = 0
    for r in rows:
        #print(r)
        print(f" {r[0]}\t{r[1]}\t{r[2]}")
        total = total + r[2]
    print(total)
        

main()
