from django.db import models

# Create your models here.
class MovieModel(models.Model):
    releasedate = models.DateField()
    moviename = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    actress = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2,decimal_places=1)