"""  units                 price
     -----                 ------
    1st 100              no price
    next 100 units      Rs 5per unit
    next 200 units      Rs 10per unit """



units = int(input("enter units"))
if units <=100:
    amt = 0
elif units > 100 and units <=200:
    amt = (units-100)*5
else:
    amt = 500 +(units-200)*10

print("Total amount...",amt)
