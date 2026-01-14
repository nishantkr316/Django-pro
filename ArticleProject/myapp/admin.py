from django.contrib import admin
from myapp.models import ArticleModle

# Register your models here.
class ArticleModleAdmin(admin.ModelAdmin):
    list_display=['id','title','description','author','date']
admin.site.register(ArticleModle,ArticleModleAdmin)
