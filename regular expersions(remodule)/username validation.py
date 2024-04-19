import re

def main():
    uname = input("enter user name")
    m = re.fullmatch(r'[a-z A-Z 0-9]+',uname)
    if m != None:
        print(f"{uname} is valid")
    else:
        print(f"{uname} is in vallid")

main()
