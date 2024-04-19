import datetime as d

dt1 = d.datetime.today()
dt2 = d.datetime.now()

print(f"Today datetime{dt1}")
d1 = dt1.date()
t1 = dt1.time()
print(d1)
print(t1)
print(f"Now datetime{dt2}")
d2 = dt2.date()
t2 = dt2.time()
print(d2)
print(t2)
