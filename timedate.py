import calendar
import time
from datetime import datetime

stdmonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
stdmonthsabbr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
cd = datetime.now().day
cm = datetime.now().month
cy = datetime.now().year
dim = calendar.monthrange(cy, cm)[1] # days in the month
drm = dim-cd # days remaining in the month
cmn = stdmonths[cm-1] # current month neat. -1 for array vars starting at 0
tsb = 0 # time since beginning looping

if drm == 1:
    dpl = "day"
else:
    dpl = "days"

c_hr = datetime.now().hour
c_mn = datetime.now().minute
c_sc = datetime.now().second

if c_mn < 10:
    c_mn = '%02d' % c_mn
if c_sc < 10:
    c_sc = '%02d' % c_sc

print(f"The current time is {c_hr}:{c_mn}.{c_sc}. The current date is {cmn} {cd}, {cy}. There are {dim} days in this month, leaving {drm} {dpl} left in the month.")
print(f"\nTo stop counting, press CTRL+C at any time.")

while True:
    c_hr = datetime.now().hour
    c_mn = datetime.now().minute
    c_sc = datetime.now().second
    if c_mn < 10:
        c_mn = '%02d' % c_mn
    if c_sc < 10:
        c_sc = '%02d' % c_sc
    tsb += 1
    print(f"The current time is {c_hr}:{c_mn}.{c_sc}. This message has been displayed {tsb} times.")
    time.sleep(1)