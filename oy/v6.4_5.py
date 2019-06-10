import re
r = r"([a-z]+) ([a-z]+)"
patten = re.compile(r)
rzt = patten.match("i love python  hack")
p = rzt.group(0)
print(p)
p1=rzt.span()
print(p1)
p2=rzt.group(1)
print(p2)
p3=rzt.groups()
print(p3)