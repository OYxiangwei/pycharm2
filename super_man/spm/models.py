import time

from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):
        return self.name
class classroom(models.Model):
    roomid = models.IntegerField()
    loc = models.CharField(max_length=10)
    roomname = models.CharField(max_length=20)
    def __str__(self):
        return self.roomname

class teacher(models.Model):
    name = models.CharField(max_length=10)
    course = models.CharField(max_length=10)
    room = models.OneToOneField(classroom)
    def __str__(self):
        return self.name
    def getroomname(self):
        return self.room.roomname
    getroomname.short_description = "教室"

    def getcurtime(self):
        return time.ctime()
    getcurtime.short_description = "当前时间"