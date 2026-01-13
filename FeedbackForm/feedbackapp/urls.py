from django.urls import path
from feedbackapp import views

urlpatterns=[
    path('form/',views.form_view,name='form'),
    path('feed/',views.feedback_view,name='feedback')
]