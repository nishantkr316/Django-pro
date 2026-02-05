from django.contrib import admin
from blogapp.models import BlogModel

# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    list_display=['id','title','description','author','date']
admin.site.register(BlogModel,BlogModelAdmin)
