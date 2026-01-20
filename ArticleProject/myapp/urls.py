
from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.home_view, name='home'),
    path('form/',views.form_view ,name='form'),
    path('all_art/',views.allarticle_view, name='all_article'),
    path('spc_art/<int:id>',views.spc_article_view, name='spc_art'),
    path('del_art/<int:id>',views.delarticle_view, name='del_art'),
    path('upd_art/<int:id>',views.update_view, name='upd_art'),
    path('del_all_art/',views.del_all_art_view,name='del_all')
]