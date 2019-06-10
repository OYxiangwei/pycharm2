def say(self):
    print("事列方法")
class b():
    def say(self):
        print("leili")
class a():
    pass


a.say = say
a.say(33)
a = a()
a.say()