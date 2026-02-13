from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateField()
    banner = models.ImageField(upload_to='banners/', null=True, blank=True)

    def __str__(self):
        return self.title
