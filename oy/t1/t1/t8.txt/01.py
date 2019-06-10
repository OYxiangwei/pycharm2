class student():

    def __init__(self,name= "oy",age = 18):
        self.name = name
        self.age = age
    def say(self):
        print("{0},{1}".format(self.name,self.age))
def sayhi():
    print("hi")