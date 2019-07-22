#学生类
#say函数
#打印
class student():
    def __init__(self,name="noname",age=12):
        self.name = name
        self.age = age

    def sayhill(self):
        print("my name is {}".format(self.name))

def say():
    print("i am hackering")

print("pkg1模块this is over")