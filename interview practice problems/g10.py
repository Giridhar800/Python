# Check if the number is Armstrong number or not
# Without use power function

n =int(input("eneter the number"))
s =n
b=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1=sum1+(r**b)
    n=n//10
if s==sum1:
    print("armstrong numbeer")
else:
    print("not armstrong")

