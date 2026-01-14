
from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home_view, name='home'),
    path('form/',views.form_view ,name='form'),
    path('all_art/',views.allarticle_view, name='all_article'),
    path('spc_art/',views.spc_article_view, name='spc_art')
]