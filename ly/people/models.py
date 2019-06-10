from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=12)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    hobby = models.CharField(max_length=20)
class school(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)
    def __str__(self):
        return self.school_name

class manageman(models.Model):
    manageman_id = models.IntegerField()
    manageman_name = models.CharField(max_length=12)
    my_school = models.OneToOneField(school)
    def __str__(self):
        return self.manageman_name
class teacher(models.Model):
    teacher_name = models.CharField(max_length=30)
    my_school = models.ForeignKey("school")
class student(models.Model):
    student_name = models.CharField(max_length=20)
    my_teacher = models.ManyToManyField("teacher")