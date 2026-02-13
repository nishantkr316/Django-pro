from django.contrib import admin
from authapp.models import IDCard,Subject,ClassRoom,Student

# Register your models here.
@admin.register(IDCard)
class IDCardAdmin(admin.ModelAdmin):
    list_display=['id','card_number']
    list_display_links=['card_number']
    search_fields=['name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['id','name']
    search_fields=['name']

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display=['id','name']
    search_fields=['name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','id_card','classroom']
    list_display_links=['name']
    search_fields=['name']
    list_filter=['classroom']
    filter_horizontal=['subject']


