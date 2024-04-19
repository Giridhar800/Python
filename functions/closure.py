def find_power(num):
    def power(p):
        return num**p
    return power

def main():
    p1 = find_power(2)(3)
    #res1 = p1(2)
    #res2 = p1(3)
    #print(res1,res2) # methods usefull
    print(p1)

main()
