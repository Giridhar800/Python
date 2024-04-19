num_list = [1,6,8,4,6,3,2,12,11,67,45,67,98,45,34,42,50]

evenlist = [value for value in num_list if value%2 == 0]
oddlist = [value for value in num_list if value%2 != 0]

print(num_list)
print(f"even list=>{evenlist}")
print(f"odd list=>{oddlist}")
