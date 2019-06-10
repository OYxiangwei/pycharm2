import time ,threading
lock_1 = threading.Lock()
lock_2 = threading.Lock()
def func1():
    print("func1 start ")
    lock_1.acquire()
    print("func1 申请锁1")
    lock_2.acquire()
    time.sleep(5)
    print("fun1申请锁2")
    lock_1.release()
    print("fun1 释放锁1")
    lock_2.release()
    print("fun1释放锁2")

def func2():
    print("func2 start ")
    lock_1.acquire()
    print("func2 申请锁1")
    rst = lock_2.acquire(timeout=2)
    if rst:
        print("fun2申请锁2成功")
        lock_2.release()
    else:
        print("func2 注定申请不到锁2")
    time.sleep(1)
    lock_1.release()
    print("fun2 释放锁1")
if __name__ == "__main__":
    tr_1 = threading.Thread(target=func1,args=())
    tr_2 = threading.Thread(target=func2,args=())
    tr_1.start()
    tr_2.start()
    tr_1.join()
    tr_2.join()