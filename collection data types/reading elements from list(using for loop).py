num_list = [2,7,9,4,6,3,11,16,17,23,53,98]
even_count = 0
odd_count = 0

for i in num_list:
    if i%2 == 0:
        even_count += 1
    else:
        odd_count +=1

print(f" Even count =>>{even_count}")
print(f" Even count =>>{odd_count}")
