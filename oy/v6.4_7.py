import re
pattern = re.compile(r'\d+')
rzt = pattern.search("2 i love 3 you 56")
print(rzt.group())