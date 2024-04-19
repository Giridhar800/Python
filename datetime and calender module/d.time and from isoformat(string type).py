import datetime as d

t1 = d.time(6,30,8)
print(t1)
print(t1.hour,t1.minute,t1.second)

t2 = d.time.fromisoformat("06:27:30")
print(t2)
print(t2.hour,t2.minute,t2.second)
