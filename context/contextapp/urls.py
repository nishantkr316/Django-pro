from django.urls import path
from contextapp import views

urlpatterns=[
    path('home/',views.home_view),
    path('java/',views.java_view),
    path('python/',views.python_view)
]