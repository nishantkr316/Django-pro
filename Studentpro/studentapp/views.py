from django.shortcuts import render,redirect
from studentapp.models import Student,Course
# Create your views here.
def home_view(request):
    type='home'
    return render(request,'home.html',{'type':type})

def course_view(request):
    courses=Course.objects.all()
    type='Course'
    return render(request,'course.html',{'type':type,'courses':courses})

def student_course_view(request):
    students=Student.objects.all()       
    type='Student-Course'
    return render(request,'allstudent.html',{'type':type,'students':students})

def studentfilter_view(request,id):
    type='Filter'
    student=Student.objects.get(id=id)
    Courses=student.course_set.all()
    return render(request,'sfilter.html',{'type':type,'student':student,'courses':Courses})

def coursefilter_view(request,id):
    type='Filter'
    course=Course.objects.get(id=id)
    all=course.student.all()
    return render(request,'cfilter.html',{'type':type,'course':course,'students':all})

def delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('student_course')


        