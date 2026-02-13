from django.urls import path, include
from artapp import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('addart/', views.article_create, name='addart'), 
    path('allart/', views.allarticle_list, name='articles'),
    path('filart/<int:id>/', views.filter_article, name='filart'),
    path('upart/<int:id>/', views.article_update, name='upart'),              
    path('delart/<int:id>/', views.delete_article, name='delart'),
    path('delallart/', views.delall_article, name='delallart'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('new_password/',views.new_password,name='new_password')
]