x = 100
def fun1():
    x = 200
    print(x)
    d = globals()
    print(d['x'])
    d['x'] = 300

fun1()
print(x)
