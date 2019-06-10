import re

t = re.compile(r"\d+")
ret = t.match("22dds33da2",5,33)
print(ret)
print(ret[0],ret.start(0),ret.end(0))

t1 = re.compile(r"([a-z]+) ([a-z]+)",re.I)
rzt = t1.match("i love you ")
print(rzt)
print(rzt.groups(),rzt.group(),rzt.start(0),rzt.end(0))

t2 = re.compile(r"\d+")
rt = t2.search("2heh65eh",0,12)
print(rt)
print(t2.findall("4ewe3r76qr",0,12))
rt2 = t2.finditer("823sew65erw",1,12)
for i in rt2:
    print(i)

r2 = re.compile("(\w+) (\w+)")

s = "i love you"
print(r2.sub(r"you like",s))

wo = "欧阳文宸 is superman"
pt = re.compile(r"[\u4c00-\u9fa5]+")
print(pt.findall(wo))

p1 = re.compile(r"<div>.*</div>")
p2 = re.compile(r"<div>.*?</div>")
title = "<div>name</div><div>age</div>"
print(p1.search(title))
print(p2.search(title))