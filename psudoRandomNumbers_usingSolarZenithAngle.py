import math
from datetime import datetime as dt

lat=23.000001

day_of_year = dt.now().timetuple().tm_yday
noww = dt.now()
now=noww.strftime("%d/%m/%Y %H:%M:%S")
hour=day_of_year*24
hrs=noww.strftime("%H")
minu=noww.strftime("%M")
print(now,day_of_year,hrs,hour)
y = (2*(math.pi)/365)*(int(day_of_year) - 1 + (int(hour)-12)/24)


print(y)
eqtime = 229.18*(0.000075+0.001868*math.cos(y)-0.032077*math.sin(y)-0.014615*math.cos(2*y)-0.040849*math.sin(2*y))
declin = 0.006918-(0.399912*math.cos(y))+(0.070257*math.sin(y))-(0.006758*math.cos(2*y))+(0.000907*math.sin(2*y))-(0.002697*math.cos(3*y))+(0.00148*math.sin(3*y))
                 
time_offset = eqtime - 4*lat + 60*(5.5)
tst = eval(hrs)*60 + eval(minu) + time_offset
ha = tst/4 - 180
Phi = math.sin(lat)*math.sin(declin)+math.cos(lat)*math.cos(declin)*math.cos(ha)

for i in range(10):
    print(math.cos(Phi))
