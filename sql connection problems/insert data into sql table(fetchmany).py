import mysql.connector as m
def main():
    cn = m.connect(database = 'sychoyadav',user = 'root',password = 'giri')
    c = cn.cursor()
    values = [(107,"eee",100,10),
              (108,"eee2",200,30)]
    c.executemany("insert into employee values(%s,%s,%s,%s)",values)
    print(c.rowcount)
    cn.commit()
    cn.close()
main()
    
