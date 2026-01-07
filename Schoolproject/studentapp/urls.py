from django.urls import path
from studentapp import views

urlpatterns=[
    path('data/',views.student_View)
]