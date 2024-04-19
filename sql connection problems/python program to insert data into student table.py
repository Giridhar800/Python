import mysql.connector as m
def main():
    cn = m.connect(database = 'sychoyadav',user = 'root',password = 'giri')
    print("connection established...")
    c = cn.cursor()
    c.execute("insert into student values(101,'ggg1',3000.00)")
    
    print(c.rowcount)
    cn.commit()
    cn.close()

main()
    
