from django.db import models


# Create your models here.
class FeedbackModel(models.Model):
    name=models.CharField(max_length=50)
    feed=models.TextField()