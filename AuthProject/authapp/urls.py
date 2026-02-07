from django.urls import path
from authapp import views
from django.contrib.auth import views as auth_view   #inbuilt Views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('about/',views.about_view,name='about'),
    path('recent/',views.recent_view,name='recent'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('new_password/',views.new_password,name='new_password'),


#For Password Change

    path("change_password/",
         auth_view.PasswordChangeView.as_view(
         template_name ='change_password.html',
         success_url ='/'
         ),
         name ="change_password"
    )
]