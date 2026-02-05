from django.urls import path
from movieapp import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('form/',views.movie_form,name='form'),
    path('all/',views.all_movies,name='movies'),
    path('update/<int:id>',views.update_movie,name='update'),
    path('delete/<int:id>',views.del_movie,name='delete'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('login/',views.login_view,name='login'),
    path('mhome/',views.mov_home_view,name='mhome'),

]