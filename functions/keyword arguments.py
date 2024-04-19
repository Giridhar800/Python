def add(*values,**kwargs):
    s = 0
    for v in values:
        s = s+v
    for v in kwargs.values():
        s = s+v
    return s

def main():
    res1 = add(10,20,30)
    res2 = add(a=20,b=10,c=30)
    res3 = add(10,20,30,x=40,y=50)
    print(res1,res2,res3,sep = "\n")

main()
