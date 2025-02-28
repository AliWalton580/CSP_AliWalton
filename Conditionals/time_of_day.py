# Ali Walton, Time of Day Python

import time
current = time.time()
local_time = time.localtime(current)
hour = local_time.tm_hour


if  hour >=12 and hour < 17 :
    print("Good afternoon!")
elif hour >= 17 :
     print("Good Evening!")
else:
    print("Good morning!")