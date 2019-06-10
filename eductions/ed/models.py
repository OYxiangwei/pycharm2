from django.db import models

# Create your models here.
class teacher(models.Model):
    teacher_id = models.IntegerField()
    teacher_name = models.CharField(max_length=33)

    def __str__(self):
        return self.teacher_name

class school(models.Model):
    school_name=models.CharField(max_length=23)
    school_ali = models.CharField(max_length=22)
    myschool = models.OneToOneField(teacher)
    def __str__(self):
        return self.school_name
