import threading
loop = 1000
s = 0
lock = threading.Lock()
def sum():
    global loop , s
    for i in range(1,loop):
        lock.acquire()
        s +=1
        lock.release()
def min():
    global loop, s
    for i in range(1,loop):
        lock.acquire()
        s -=1
        lock.release()

if __name__=="__main__":
    print(s)
    s1 = threading.Thread(target=sum,args=())

    s1.start()
    s2 = threading.Thread(target=min,args=())

    s2.start()
    s1.join()
    s2.join()
    print(s)
