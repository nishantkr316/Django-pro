from django.contrib import admin
from myapp.models import StudentModel   

# Register your models here.
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'sub', 'rollno']
