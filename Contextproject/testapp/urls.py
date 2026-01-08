from django.urls import path
from testapp import views
urlpatterns=[
    path('home/',views.home_view),
    path('python/',views.python_view),
    path('java/',views.java_view),
    path('js/',views.js_view)
]