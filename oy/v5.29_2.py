import threading
import asyncio

@asyncio.coroutine
def hello():
    print("hello world %s"%threading.currentThread())
    print("start .....%s"%threading.currentThread())
    yield from asyncio.sleep(10)
    print("done  (%s)"%threading.currentThread())
    print("hello agein(%s)"%threading.currentThread())
loop = asyncio.get_event_loop()
tasks = [hello(),hello()]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()