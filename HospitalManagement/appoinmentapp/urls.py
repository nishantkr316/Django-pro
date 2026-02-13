from django.urls import path
from appoinmentapp import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('doctor/',views.doctor_view,name='doctor'),
    path('patient/',views.patient_view,name='patient'),
    path('appoinment/',views.appoinment_view,name='appoinment'),
    path('docappoinment/<int:id>',views.doc_appoinment_view,name='docappoinment'),
    path('patappoinment/<int:id>',views.pat_appoinment_view,name='patappoinment'),
]