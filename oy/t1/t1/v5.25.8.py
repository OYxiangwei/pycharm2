from datetime import datetime ,timedelta
import time
import timeit

#dt = datetime(2018,5,25)
#print(dt.today())
#print(dt.now())
#print(dt.fromtimestamp(time.time()))

#t = datetime.now()
#td = timedelta(hours = 3)
#print((t + td).strftime("%Y%m%d %H:%M"))
c = '''
sum = []
for i in range(1000):
    sum.append[i]
'''
t1 = timeit.timeit(stmt="[i for i in range(1000)]",number=1000)
t2 = timeit.timeit(stmt=c,number=1000)
print(t1)