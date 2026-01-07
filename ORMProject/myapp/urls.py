from django.urls import path
from myapp import views

urlpatterns=[
    path('data/',views.employee_View)
]