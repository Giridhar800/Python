import calendar as c

f = open("month_cal.html","w")
hcal = c.HTMLCalendar()
mcal = hcal.formatmonth(2024,12)
print(mcal,file = f,flush = True)
