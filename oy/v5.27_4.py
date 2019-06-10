import threading
import time


class mythread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if lock_1.acquire(1):
            num = num +1
            msg = self.name + "set num to "+ str(num)
            print(msg)
            lock_1.acquire()
            lock_1.release()
            lock_1.release()
lock_1 = threading.RLock()
num = 0

def ytest():
    for i in range(5):
        t = mythread()
        t.start()
if __name__ =="__main__":
    ytest()