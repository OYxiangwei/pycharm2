
import timeit

c = '''
def sum(num):
    for i in range(num):
        i+=i
        print(i)
'''
t1 = timeit.timeit(stmt="[i for i in range(1000)]",number=100000)
t2 = timeit.timeit("sum(num)",setup=c+"num=100",number=100)
print(t1,"-",t2)