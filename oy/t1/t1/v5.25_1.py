class tulingMetaClass(type):

    def __new__(cls,name,bases,attrs):
        print("我是 元类啊")
        attrs["id"] = 1111

        attrs["addr"] = "beijinroad"
        return type.__new__(cls,name , bases,attrs)

class teacher(object,metaclass = tulingMetaClass):
    pass
t = teacher()
t.id
print(t.id)
