import pickle

def main():
    f = open("datafile1.ser","rb")
    obj1 = pickle.load(f)
    print(obj1,type(obj1))
    obj2 = pickle.load(f)
    print(obj2,type(obj2))
    obj3 = pickle.load(f)
    print(obj3,type(obj3))

main()
