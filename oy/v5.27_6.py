import os
from multiprocessing import Process
def info(title):
    print(title)
    print(__name__)
    print(os.getpid())
    print(os.getppid())

def f(n):
    info(n)

if __name__=="__main__":
    info("文宸")
    p = Process(target=f,args=("oy",))
    p.start()
    p.join()