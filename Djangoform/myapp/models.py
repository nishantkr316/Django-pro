from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    sub = models.CharField(max_length=50)
    rollno = models.IntegerField()
    
