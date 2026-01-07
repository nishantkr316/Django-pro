from django.contrib import admin
from studentapp.models import StudentModel

# Register your models here.
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['id','name','dob','email','city','add']


admin.site.register(StudentModel,StudentModelAdmin)