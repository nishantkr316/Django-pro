from django.urls import path
from Newsapp import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('bussiness/',views.bussiness_view,name='bussiness'),
    path('sports/',views.sports_view,name='sports'),
    path('entertainment/',views.entertainment_view,name='entertainment')
]