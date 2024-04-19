def main():
    f = open("std.txt","a")
    while True:
        rollno = int(input("enter roll no:"))
        name = input("enter name")
        course = input("enter course")
        print(rollno,name,course,file = f)

        ans = input("Add another student")
        if ans == "no":
            f.close()
            break

main()
