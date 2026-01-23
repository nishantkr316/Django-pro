from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.student_view, name='student'),
    path('contact/', views.contact_view, name='contact'),
]