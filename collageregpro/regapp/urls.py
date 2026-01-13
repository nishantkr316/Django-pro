from django.urls import path
from regapp import views

urlpatterns=[
    path('form/',views.form_view ,name='form'),
    path('data/',views.studentdata_view, name='data')
]