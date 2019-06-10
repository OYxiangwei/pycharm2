from django.db import models

# Create your models here.
class xwmodel(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=20)
    hebby = models.CharField(max_length=20)

    def __str__(self):
        return self.name