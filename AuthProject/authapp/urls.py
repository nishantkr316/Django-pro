from django.urls import path
from authapp import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('about/',views.about_view,name='about'),
    path('recent/',views.recent_view,name='recent'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
]