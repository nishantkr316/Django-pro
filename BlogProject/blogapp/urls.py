from django.urls import path
from blogapp import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('addblog/',views.addblog_view,name='addblog'),
    path('allblog/',views.allblog_view,name='allblog'),
    path('filtblog/<int:id>',views.filterblog_view,name='filtblog'),
    path('upblog/<int:id>',views.updateblog_view,name='upblog'),
    path('delblog/<int:id>',views.delblog_view,name='delblog'),
    path('alldelblog/',views.delallblog_view,name='alldelblog')
]