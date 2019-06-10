import json
data = {"name":"Anonymous","age":29}
with open (r"t.json","w")as f:
    json.dump(data,f)

with open(r"t.json","r")as f:
    d = json.load(f)
    print(d)
