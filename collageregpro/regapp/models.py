from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobno=models.IntegerField()
    sub=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    add=models.CharField(max_length=100)

