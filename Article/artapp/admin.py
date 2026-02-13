from django.contrib import admin
from .models import ArticleModel

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
admin.site.register(ArticleModel, ArticleAdmin)
