from django.contrib import admin
from myapp.models import EmployeeModel

# Register your models here.
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display=['id','ename','email','city','address','company','salary','jobrole']



admin.site.register(EmployeeModel,EmployeeModelAdmin)
