from django.contrib import admin
from appoinmentapp.models import Doctor,Patient,Appoinment

# Register your models here.
@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Patient)
class Patient(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Appoinment)
class Appoinment(admin.ModelAdmin):
    list_display=['id','doctor','patient','date']
