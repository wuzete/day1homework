from django.db import models

# Create your models here.


class User(models.Model):
    headpic = models.ImageField(upload_to="media")
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)