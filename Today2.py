from datetime import date
import time

today = date.today()
#print("Today's Date: ", today)

d1 = today.strftime("%d/%m/%Y")
#print("Today's Date: ", d1)

d2 = today.strftime(("%B %d, %Y"))
#print("Today's Date: ", d2)

d3 = today.strftime("%m/%d/%y")
#print("Today's Date: ", d3)

d4 = today.strftime("%b-%d-%Y")
#print("Today's Date: ", d4)

#For 24hrs Format:
t = time.localtime()
c_t = time.strftime("%H:%M:%S",t)
print(c_t)

#For 12hrs format:
t = time.localtime()
ct_t = time.strftime("%-I:%M %p",t)
print(ct_t)
