from collections.abc import Iterable,Iterator
l = [1,2]
il = iter(l)
print(isinstance(l,Iterable))
print(isinstance(il,Iterator))
print(isinstance(il,Iterable))

l = [i for i in range(3)]
g = (i for i in range(3))
print(type(l))
print(type(g))


def y():
    yield 1
    yield 2
    yield 3



fun5=y()
print(next(fun5))
print(next(fun5))
print(next(fun5))

def fib(max):
    n,a,b = 0 ,0 ,1
    while n<max:
        yield b
        a,b = b,a+b
        n +=1
    return "dohe"

g = fib(5)
for i in range(6):
    rst = next(g)
    print(rst)