import mysql.connector as m

def main():
    cn = m.connect(database = 'sychoyadav',user = 'root',password = 'giri')
    c = cn.cursor()
    r = int(input("enter rollnumber"))
    c.execute("delete from student where rollno = %s",params = [r])
    if c.rowcount == 1:
        print("student deleted...")
        cn.commit()
        cn.close()
    else:
        print("invallid rollno...")

main()
