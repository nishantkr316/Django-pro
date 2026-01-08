from django.urls import path
from myportfolio import views

urlpatterns=[
    path('',views.base_view,name='base'),
    path('home/',views.home_view, name='home'),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact'),
    path('blog/',views.blog_view, name='blog')
]