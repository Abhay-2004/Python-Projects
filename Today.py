from datetime import date; import datetime
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

now = datetime.datetime.now()
c_t = now.strftime("%H:%M:%S")
print("Current Time: ", c_t)