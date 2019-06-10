from collections import namedtuple

ResClass = namedtuple("res","count average")

def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        if term is None:
            break
        total +=term
        count +=1
        average = total/count
    return ResClass(count,average)
def grouper(storages,key):
    while True:
        storages[key] = yield from averager()
def client():
    process_data = {
        "boy_2":[29.0,40.8,11.2,22.4],
        "boy_1":[2.1,3.1,4.2,2.1]
    }
    storages = {}
    for k,v in process_data.items():
        coroutine = grouper(storages,k)
        next(coroutine)
        for dt in v:
            coroutine.send(dt)
        coroutine.send(None)
    print(storages)

client()