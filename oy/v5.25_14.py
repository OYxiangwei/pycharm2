import time
def printtime(f):
    def wrapper(*args,**kwargs):
        print("time:",time.ctime())
        return f(*args,**kwargs)
    return wrapper

#@printtime
#def hello():
    print("hello,world")
def hello3():
    print("手动")

hello3=printtime(hello3)
hello3()

#hello()

print(int("101011101",base=2))


def int8(x):
    return int(x,base=8)


print(int8("2222"))

import functools

int16 = functools.partial(int,base=16)
print(int16("2223132"))

def add(x,y):
    return x+y
addone =functools.partial(add,1)
print(addone(3))


l1 = [i for i in range(0,10)]
l2 = [j for j in range(11,20)]

l3 = zip(l1,l2)

print(type(l3))
print(l3)
for k in l3:
    print(k)

print([z for z in l3])


l4 = ["o","y","w","c"]

em = enumerate(l4,start = 77)
print(em)
l5 =[y for y in em]
print(l5)
