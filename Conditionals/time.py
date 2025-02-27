# Ali Walton, How to get the time of day

import time

 #first instance of time in programming
#print(time.gmtime(0)

#current time in seconds since gmtime
#print(time.time())

#current time as we are used to seeing it
current = time.time()
now = time.ctime(current)
print(now)

#get just the hour
local_time = time.localtime(current)
#print(local_time)
hour = local_time.tm_hour
minutes = local_time.tm_min
print(hour)