import mysql.connector as m

def main():
    cn = m.connect(database = 'sychoyadav',user = 'root',password = 'giri')
    c = cn.cursor()
    r = int(input("enter rollnumber"))
    f = float(input("enter update fees"))
    c.execute("update student set fees = %s where rollno = %s",params = [f,r])
    k = c.rowcount
    print(k)
    if k > 0:
        print("updated...")
        cn.commit()
    else:
        print("invallid rollno")
    cn.close()
main()
    
    
