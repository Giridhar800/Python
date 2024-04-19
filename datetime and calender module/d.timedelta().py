import datetime as d

d1 = d.date(2014,1,11)
print(d1)
days = d.timedelta(days = 10)
d1 = d1 + days

print(f"10 days add {d1}")

d2 = d1 - days
print(f"10 days sub {d2}")

m = d.timedelta(weeks = 4)
print(m)
d3 = d1 + m
print(f"4 monts add {d3}")
d4 = d1 - m
print(f"4 monts sub {d4}")

