from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    score = models.IntegerField()
    def __str__(self):
        return self.name