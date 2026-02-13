from django.urls import path
from studentapp import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('course/',views.course_view,name='course'),
    path('student_course/',views.student_course_view,name='student_course'),
    path('filter/<int:id>/',views.studentfilter_view,name='filter'),
    path('coursefilter/<int:id>/',views.coursefilter_view,name='coursefilter'),
    path('delete/<int:id>/',views.delete_view,name='delete'),

]