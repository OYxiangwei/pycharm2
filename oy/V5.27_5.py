import multiprocessing
from time import sleep,ctime
class myclock(multiprocessing.Process):
    def __init__(self,interval):
        super().__init__()
        self.interval = interval
    def run(self):
        while True:
            print("the time is %s"%ctime())
            sleep(self.interval)

if __name__ =="__main__":
    p = myclock(2)
    p.start()
