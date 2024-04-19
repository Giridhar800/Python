import calendar as c

f = open("year_cal.html","w")
hcal = c.HTMLCalendar()
ycal = hcal.formatyear(2024)
print(ycal,file = f,flush = True)
