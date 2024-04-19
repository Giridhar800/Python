import pickle

def main():
    a = 100
    b = 1.5
    c = 1+2j
    f = open("datafile1.ser","wb")
    pickle.dump(a,f)
    pickle.dump(b,f)
    pickle.dump(c,f)
    f.close()
main()
