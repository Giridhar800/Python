emp = {"giri":10000,
       "venkey":20000,
       "raju":30000,
       "krishna":40000,
       }
print(emp)
names = emp.keys()
s = emp.values()
d = emp.items()
print(names,s,d,sep="\n")

# setdefault key

dict1 = {1:10,2:20,3:30}
print(dict1)
print(dict1[1],dict1[3],sep='\n')
value = dict1.setdefault(4,100)
print(value)
