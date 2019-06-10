import re

r = r"\d+"
p = re.compile(r,re.I)
rzt = p.search("23223dasdfeawe232421314",17,29)
print(rzt.group())