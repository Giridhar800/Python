import calendar as c

f = open("calandertext.txt","w")
ycal = c.calendar(2024,m = 4)
print(ycal,file = f, flush = True)
