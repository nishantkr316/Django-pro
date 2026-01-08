from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    sub=models.CharField(max_length=50)
    mob=models.IntegerField()
    email=models.EmailField()
    city=models.CharField(max_length=30)
    add=models.CharField(max_length=100)
    isactive=models.BooleanField(default=False)