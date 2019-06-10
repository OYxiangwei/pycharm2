import random

print(random.random())
print(random.randint(1,10))
l = [str(i)+"oy" for i in range(10)]
print(random.choice(l))
l3 = [n for n in range(19)]
print(l3)
random.shuffle(l3)
print(l3)