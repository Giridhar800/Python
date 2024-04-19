import os
def main():
    old = input("enter old filename")
    new = input("enter new filename")
    os.rename(old,new)
    print("file renamed...")
main()
