from django.urls import path
from myapp import views

urlpatterns=[
    
    path('data/',views.retrive_data),
    path('filter/',views.fiter_data),
    path('agg/',views.aggregate_view)
]