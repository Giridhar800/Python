test_list = [(5,6),(5,7),(6,8),(6,10),(7,13)]
print("Original list is =>",test_list)

res = []
for sub in test_list: #(5,6)
    if res and res[-1][0] == sub[0]: # 5 == 5
        res[-1].extend(sub[1:])   #(5,6,7)   
    else:
        res.append([ele for ele in sub])#(5,6)
res = list(map(tuple,res))
print("The extracted elements:" + str(res))
