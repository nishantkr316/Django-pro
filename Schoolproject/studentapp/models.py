from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    dob=models.IntegerField()
    email=models.EmailField()
    city=models.CharField(max_length=50)
    add=models.CharField(max_length=100)
    
