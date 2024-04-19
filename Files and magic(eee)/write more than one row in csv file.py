import csv

def man():
    f = open("D:\Desktop\practice\magic(eee)\student1.csv","a",newline = "")
    w = csv.write(f)
    studentdata = [['rollno','name'],
                   [1,'giri'],
                   [2,'venkey']]
    w.writerows(studentdata)
    f.close()
main()
