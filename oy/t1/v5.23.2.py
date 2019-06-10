class A():
    def __init__(self,name="oy"):
        self.name= name
        print("by call构造函数")
        print(self.name)
    def __call__(self):
        print("by call too对象当函数使用")
    def __str__(self):
        return"直接打印对象"
    def __getattr__(self,item):
        print("未设置")
    def __setattr__(self,key,value):
        super().__setattr__(key,value)
        print(key,value)
        return None
    def __gt__(self,age):
        return self > self.age
    def eat(self):
        print("事列方法")
    @classmethod
    def say(cls):
        print("类方法")
    @staticmethod
    def play():
        print("静态方法")

a = A()
print(a.age)
a.mm = 12
A.say()
a.say()
A.play()
a.play()
a.eat()
