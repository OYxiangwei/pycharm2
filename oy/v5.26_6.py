import time , threading
print("main start:{}".format(time.ctime()))
def f():
    print("start time :{}".format(time.ctime()))
    time.sleep(3)
    print("end time:{}".format(time.ctime()))

f = threading.Thread(target=f,args=())
#f.setDaemon(True)
f.start()
time.sleep(1)
print("main end at :{}".format(time.ctime()))

