from django.urls import path
from astroapp import views

urlpatterns=[
    path('horo/',views.horoscopr_view,name='horo'),
    path('home/',views.home_view,name='home')
]