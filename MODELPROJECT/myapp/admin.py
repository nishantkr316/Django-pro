from django.contrib import admin
from myapp.models import Studentmodel

# Register your models here.


class StudentModelAdmin(admin.ModelAdmin):
    list_display=['id','name','roll_no','subject','address','email','is_active']

admin.site.register(Studentmodel,StudentModelAdmin)
