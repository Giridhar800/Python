import datetime as d
# import pdb;
# pdb.set_trace()
breakpoint()
d1 = d.date.today()
print(d1)
# important

print(d1.strftime("%a"))
print(d1.strftime("%A"))
print(d1.strftime("%w"))
print(d1.strftime("%d"))
print(d1.strftime("%d %A"))
print(d1.strftime("%d %A %b"))
print(d1.strftime("%d %A %B"))
print(d1.strftime("%d/%m"))
print(d1.strftime("%d/%m/%y"))
print(d1.strftime("%d/%m"))
print(d1.strftime("%d %A %B %Y"))
print()

dt = d.datetime.today()
print(dt)
print(dt.strftime("%H %M %S"))
print(dt.strftime("%j"))
print(dt.strftime("%U"))
print(dt.strftime("%W"))
print(dt.strftime("%x"))
print(dt.strftime("%X"))






