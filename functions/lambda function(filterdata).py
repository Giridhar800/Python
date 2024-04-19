def filter_data(l,f):
    l1 = []
    for value in l:
        if f(value):
            l1.append(value)
    return l1

def main():
    list1 = [12,15,18,9,5,7,3,12,14,16,20,22,24]
    list2 = filter_data(list1,lambda num:num%2 == 0)
    list3 = filter_data(list1,lambda num:num%2 != 0)
    list_str = ['a','b','c','A','B','C']
    list4 = filter_data(list_str,lambda s:s.islower())
    print(list1)
    print(list2)
    print(list3)
    print(list4)

main()
