import time
import _thread as thread
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

def main():
    print("start time{}".format(time.ctime()))
    thread.start_new_thread(lop1,("欧阳文宸",))
    thread.start_new_thread(lop2,(2,3))

    time.sleep(10)
    print("end time :{}".format(time.ctime()))

if __name__ =="__main__":
    main()
