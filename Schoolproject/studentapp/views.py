from django.shortcuts import render
from studentapp.models import StudentModel

# Create your views here.
def student_View(request):
    all_data=StudentModel.objects.all()
    context={"student_data":all_data}
    return render(request,'student.html',context)