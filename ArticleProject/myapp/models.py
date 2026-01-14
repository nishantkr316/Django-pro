from django.db import models

# Create your models here.
class ArticleModle(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    author=models.CharField(max_length=50)
    date=models.DateField()
