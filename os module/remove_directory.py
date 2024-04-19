import os
dname = input("directory name of folder name")
try:
    os.rmdir(dname)
    print("directory is removed")
except osError:
    print("directory is not empty")
    
