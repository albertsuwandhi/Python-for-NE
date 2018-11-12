#/usr/bin/env python
import datetime
print("Current date/time :", str(datetime.datetime.now()))
now = datetime.datetime.now()
output = now + datetime.timedelta(minutes=100)
print("Current date/time + 100 minutes:", output)
print("2 weeks from now:", str(datetime.datetime.now()+datetime.timedelta(weeks=2)))



