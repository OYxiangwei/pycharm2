import time
import threading
def lop1(m):
    print("lop1 start time:{}".format(time.ctime()))
    print(m)
    time.sleep(3)
    print("lop1 end time:{}".format(time.ctime()))
def lop2(m,n):
    print("lop2 start time:{}".format(time.ctime()))
    print(m,n)
    time.sleep(4)
    print("lop2 end time:{}".format(time.ctime()))
def lop3():
    print("lop3 start time:{}".format(time.ctime()))
    time.sleep(5)
    print("lop3 end time:{}".format(time.ctime()))

def main():
    print("start time:{}".format(time.ctime()))
    t1 = threading.Thread(target=lop1,args=("oy",))
    t1.setName("th_1")
    t1.start()
    t2 = threading.Thread(target=lop2,args=("hacker","Anonymous"))
    t2.setName("th_2")
    t2.start()
    t3 = threading.Thread(target=lop3,args=())
    t3.setName("th_3")
    t3.start()
    #t1.join()
    #t2.join()
    #t3.join()
    for th in threading.enumerate():
        print("运行的是:{}".format(th.getName()))
    print("现在运动的线程是:{}".format(threading.currentThread()))
    print("有多少个线程在跑:{}".format(threading.activeCount()))
    print("\n all end time:{}".format(time.ctime()))


if __name__=="__main__":
    main()
    while True:
        time.sleep(10)
