import random
def multen(n):
    return n*10
l = [i for i in range(10)]

l2 = map(multen,l)
print(l2)
for i in l2:
    print(i)
l3 = [j for j in l2]

from functools import reduce
def sum(x,y):
    return x+y

print(reduce(sum,(2,3,4)))

def iseven(a):
    return a%2==0

l8 = filter(iseven,l)
print([z for z in l8])
random.shuffle(l)
print(l)
print(sorted(l))
print(sorted(l,reverse=True))
print(sorted(l,key=abs,reverse= True))

l7 = ["a","b","d","c"]
print(sorted(l7,key=str.lower,reverse=True))

def my1():
    def d():
        print("in d")
        return 3
    return d()
my1()

def my5( *args):
    def my8():
        rst = 0
        for p in args:
            rst += p

        return rst
        print(rst)
    return my8()
my5(3,4)



def count2():
    def f(j):
        def g():
            return j*j
        return g

    k = []
    for o in range(1,4):
        k.append(f(o))
    return k

f1,f2,f3 =count2()
print(f1(),f2(),f3())