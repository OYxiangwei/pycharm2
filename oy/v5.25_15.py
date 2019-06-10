import collections
point = collections.namedtuple("Point",['x','y'])
p = point(12,13)
print(p[0])
print(p.x)


C = collections.namedtuple("ciycle",['x','y','r'])
clycle = C(2,3,4)
print(clycle)
print(isinstance(clycle,tuple))


from collections import deque

q = deque(["q","a","c","d"])
print(q)
q.append("k")
print(q)
q.appendleft("hacker")
print(q)

f = lambda x : x*10
print(f(2))
from collections import defaultdict
d2 = lambda : "欧阳文宸"
d2 = defaultdict(d2)
d2["one"] = 1
print(d2["one"])
print(d2["three"])

from collections import Counter

c  = Counter("1131312sadfadfawerqsdadaerqrqwe")
print(c)
print(c["q"])


f = open("t1.txt","w")
f.close()

with open(r't1.txt','w')as f:
    strline = f.writelines("hacker")
    strline = f.writelines("\noyxw")
    strline = f.writelines("\n欧阳文宸")

with open(r't1.txt','r')as fl:
    strline =fl.readline()
    while strline:
        print(strline)
        strline=fl.readline()


with open(r't1.txt','r')as k:
    z = list(k)
    for d in z:
        print(d)


with open(r't1.txt','r')as j:
    str3 = j.read(2)
    print(str3)

with open(r't1.txt','r')as b:
    b.seek(6,0)
    str4 = b.read()
    print(str4)

import time

with open(r't1.txt','r')as e:
    str6 =e.read(1)
    while str6:
        time.sleep(1)
        print(str6)
        str6 =e.read(1)

with open(r't1.txt','r')as i:
    str9 = i.read(2)
    pos = i.tell()
    while str9:
        print(str9)
        print(pos)
        str9=i.read(2)
        pos=i.tell()