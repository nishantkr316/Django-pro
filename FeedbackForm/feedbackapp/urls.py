from django.urls import path
from feedbackapp import views

urlpatterns=[
    path('form/',views.form_view),
    path('feed/',views.feedback_view)
]