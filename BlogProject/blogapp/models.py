from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    bloger=models.CharField(max_length=70)
    date=models.DateField()
