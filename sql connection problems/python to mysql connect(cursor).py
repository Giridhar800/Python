import mysql.connector
def main():
    cn = mysql.connector.connect(database = 'sychoyadav',user = 'root',password = 'giri')
    print("connection established...")
    c = cn.cursor()
    print("cursor is created...")
    print(type(c))

main()
    
