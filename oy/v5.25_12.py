s = lambda x,y,z:x*100+y/z
#print(s(2,3,4))

def funa(n):
    return n * 100

def funb(n):
    return funa(n)*3

def func(n,k):
    return n + k


#print(funb(2))
print(func(funa(1),funb(2)))
