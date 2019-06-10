import time ,re ,os,datetime
from concurrent import futures
def wait(argument):
    print(argument)
    time.sleep(1)
    return 'OK'

data= ["hacker",2]

ex = futures.ThreadPoolExecutor()
for i in ex.map(wait,data):
    print(i)