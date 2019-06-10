import time
print(time.timezone)
print(time.altzone)
print(time.daylight)
print(time.time())
print(time.localtime())
print(time.localtime().tm_mon)
print(time.asctime())
print(time.ctime())
print(time.mktime(time.localtime()))
#for i in range(8):
 #   print(i)
 #   time.sleep(1)
def p():
    time.sleep(10)
t1 =time.perf_counter()

p()
t2 = time.perf_counter()
print(t2 - t1)
