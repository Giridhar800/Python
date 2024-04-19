import mysql.connector
def main():
    cn = mysql.connector.connect(database = "sychoyadav",user = "root",password = "giri")
    print("connection Established")
    print(type(cn))
    
main()
