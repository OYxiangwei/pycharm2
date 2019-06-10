from types import MethodType
def say(self):
    print("shuo")

def talk(self):
    print("talk")


B = type("Bname",(object,),{"class_a":say,"class_b":talk})
class A():
    pass

#a = A()
#a.say = MethodType(say,A)
#a.say()
b = B()

b.class_a()