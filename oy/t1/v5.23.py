#x = property(fget,fset,fdel,doc)
class human():
    '''
这是类文档
    '''
    def fget(self):
        return self._name * 2
    def fset(self,name):
        self._name =name.upper()
    def fdel(self):
        self._name = "nonema"

    name = property(fget,fset,fdel,"进行以下操作")
h = human()
h.name = "dage"
print(h.name)
print(human.__dict__)
print(human.__doc__)
print(human.__name__)
print(human.__bases__)