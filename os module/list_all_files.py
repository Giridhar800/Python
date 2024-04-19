import os
import os.path
def main():
    fname = input("enter folder name")
    if os.path.exists(fname):
        if os.path.isdir(fname):
            l1 = os.listdir(fname)
            os.chdir(fname)
            f,d = 0,0
            for name in l1:
                if os.path.isfile(name):
                    f = f+1
                else:
                    d = d+1
            print(f" file count{f}")
            print(f" folder count{d}")
        else:
            print("not folder")
    else:
        print("folder does not exist")

main()
