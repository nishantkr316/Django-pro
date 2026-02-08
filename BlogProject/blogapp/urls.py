from django.urls import path
from blogapp import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('addblog/',views.addblog_view,name='addblog'),
    path('allblog/',views.allblog_view,name='allblog'),
    path('filtblog/<int:id>',views.filterblog_view,name='filtblog'),
    path('upblog/<int:id>',views.updateblog_view,name='upblog'),
    path('delblog/<int:id>',views.delblog_view,name='delblog'),
    path('alldelblog/',views.delallblog_view,name='alldelblog'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('new_password/',views.new_password,name='new_password')
]