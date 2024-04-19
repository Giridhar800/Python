import re

def main():
    email = input("enter email id")
    m = re.fullmatch(r'[a-z 0-9]+@[a-z]+\.[a-z]{3,4}',email)
    if m != None:
        print(f"{email} is vallid")
    else:
        print(f"{email} in vallid")

main()
