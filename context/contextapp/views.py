from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    context = {'skills' :['python','c','c++','java','Sql','Html','php']}
    return render(request,'base.html',context)
def python_view(request):
    return render(request,'python.html')
def java_view(request):
    return render(request,'java.html')