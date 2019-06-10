import multiprocessing
from time import ctime
def consumer(input_q):
    print("into consumer:",ctime())
    while True:
        item = input_q.get()
        if item is None:
            break
        print("pull",item,"out of q")
    print("out of consumer:",ctime())
def producer(sequence,output_q):
    for item in sequence:
        print("into producer",ctime())
        output_q.put(item)
        print("out of procuder:",ctime())
if __name__ == "__main__":
    q = multiprocessing.Queue()
    cons_1 = multiprocessing.Process(target=consumer,args=(q,))
    cons_1.start()
    cons_2 = multiprocessing.Process(target=consumer,args=(q,))
    cons_2.start()
    sequence=[1,2,3,4]
    producer(sequence,q)
    q.put(None)
    q.put(None)
    cons_1.join()
    cons_2.join()
    print(q)
