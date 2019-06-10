l = ["study hard and day day up","好好学习天天向上","明天会更好"]
with open(r"t2.txt","a")as f:
    f.writelines(l)
    f.write("\n5.26.dage")

with open(r"t2.txt","r")as f:
    #str =f.read()
    print(str)
import pickle
age = 1989
with open(r"t2.txt","wb")as f:
    pickle.dump(l,f)



with open(r"t2.txt","rb")as f:
    pickle.load(f)
    print(l)

import shelve

sh = shelve.open(r"data.db")
sh["one"]=1
sh["two"]=2
sh["three"]=3
sh.close()

sh = shelve.open(r"data.db")

try:
    print(sh["one"])
    print(sh["four"])
except Exception as e:
    print(e)
finally:
    sh.close()



import shelve
she = shelve.open(r"dd2.db")
try:
    she["one"]=["o","y","x","w","2"]
    she["two"]={"one":"快乐","two":"开心","three":"好"}
finally:
    she.close()
with shelve.open(r"dd2.db",writeback=True)as she:
    #print(she["one"])
    two =she["two"]
    print(two)
    two["one"]="wudadajiang"


with shelve.open(r"dd2.db")as she:
    print(she["two"])
