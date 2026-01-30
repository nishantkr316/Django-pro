from django.urls import path
from movieapp import views

urlpatterns=[
    path('form/',views.movie_form,name='form'),
    path('all/',views.all_movies,name='movies'),
    path('update/<int:id>',views.update_movie,name='update'),
    path('delete/<int:id>',views.del_movie,name='delete')
]