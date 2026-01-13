from django.contrib import admin
from feedbackapp.models import FeedbackModel

# Register your models here.
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display=['id','name','feed']

admin.site.register(FeedbackModel,FeedbackModelAdmin)