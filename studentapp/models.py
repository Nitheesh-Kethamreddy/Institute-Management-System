from django.db import models

# Create your models here.
class City(models.Model):
    city=models.CharField(max_length=50)

class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)
    phone = models.BigIntegerField(default=0)
    email=models.EmailField(max_length=50)
    gender=models.CharField(max_length=40)
    place=models.ForeignKey(City,on_delete=models.CASCADE)
