class person():
    name = "hacker"
    age = 12
    def say(self):
        print("hacked by oy")
    def __init__(self,name):
        self.name = name
        print("构造函数{}".format(name))
class student(person):
    name = "anonymous"

    def __init__(self):
        print("子类构造函数")
        self.setname("wangzi")
        haha()
    def setname(self,name):
        self.name = name.upper()
def haha():
    print("hhahah")

class teacher(person):
    def __init__(self,name):
        self.name = name
        self.age = 1
        self.address = "beijingroad"
        #person.__init__(self,self.name)
        super(teacher,self).__init__(self.name)
        print("扩展")
        print("天天快乐")


class personmin():
    name = "p"
    def pm(self):
        print("pm")

class studentmx():
    name = "s"
    def sm(self):
        print("sm")

class tutor(student,personmin,studentmx,):
    name = "t"
    def tm(self):
        print("tm")


t = tutor()
#t.say()
#print(issubclass(student,person))
#
#setattr(t,"name","wu")
#print(t.name)
#print(dir(t))
#print(getattr(t,"name","taizi"))
#delattr(t,"name")
print(t.name)
#print(hasattr(t,"name"))
