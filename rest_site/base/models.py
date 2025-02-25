from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True, unique=True,)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
