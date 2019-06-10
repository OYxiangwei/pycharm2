import threading
import time
semaphore = threading.Semaphore(2)

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() + "get semaphore")
        time.sleep(1)
        semaphore.release()
        print(threading.currentThread().getName() + "release semaphore")

for i in range(8):
    t1 = threading.Timer(5,func)
    t1.start()
    i = 0
    while True:
        print("{}".format(i))
        time.sleep(3)
        i +=1