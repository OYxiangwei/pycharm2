import threading

class mythread(threading.Thread):
    def __init__(self,n):
        super(mythread,self).__init__()
        self.n = n
    def run(self):
        print("my thread:{}".format(self.n))
for i in range(3):
    m = mythread(i)
    m.start()
    m.join()
print("main end")

