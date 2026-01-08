from django.db import models

# Create your models here.
class Studentmodel(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    subject = models.CharField(max_length=50)
    address = models.TextField()
    email =models.EmailField()
    is_active =models.BooleanField(default=False)

