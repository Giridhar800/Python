x = 100 # g.v
print(x)
def fun1():
    
    global x
    x = 200
    y = 300
    print(x,y)

def fun2():
    print(x)

fun1()
fun2()

