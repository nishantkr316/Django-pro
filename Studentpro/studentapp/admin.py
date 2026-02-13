from django.contrib import admin
from studentapp.models import Student,Course

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name']
    search_fields=['name']
    list_display_links=['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['id','title','content']
    search_fields=['title']
    list_display_links=['title']
    list_filter=['title']
    filter_horizontal=['student']