from django.urls import path
from studentapp import views
urlpatterns=[
    path('stu/',views.student_view)
]