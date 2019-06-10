from concurrent.futures import ThreadPoolExecutor
import time
def return_future(msg):
    time.sleep(1)
    return msg
pool = ThreadPoolExecutor(max_workers =2)
f1 = pool.submit(return_future,"hello")
f2 = pool.submit(return_future,"world")
print(f1.done())
time.sleep(3)
print(f2.done())
print(f1.result())
print(f2.result())