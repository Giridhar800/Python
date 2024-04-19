def main():
    f = open("girifile1.txt","a")
    while True:
        rollno = int(input("enter rollno"))
        name = input("enter name")
        course = input("enter course")
        print(rollno,name,course,file=f)
        ans =input("Add another std ?")
        if ans == "no":
            f.close()
            break

main()
