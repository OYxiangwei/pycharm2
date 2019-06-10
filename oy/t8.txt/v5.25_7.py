import time
from datetime import datetime as dt
t = time.localtime()

tt = time.strftime("%Y%m%d  %H:%M", t )
print(tt)
print(dt.now())