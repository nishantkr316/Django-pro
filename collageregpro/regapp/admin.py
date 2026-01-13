from django.contrib import admin
from regapp.models import StudentModel
# Register your models here.

class StudentModelAdmin(admin.ModelAdmin):
    list_display=['id','name','email','mobno','sub','city','add']

admin.site.register(StudentModel,StudentModelAdmin)
