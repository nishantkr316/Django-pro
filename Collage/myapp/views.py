from django.shortcuts import render
from myapp.models import StudentModel
# Create your views here.
def student_view(request):
    all_data=StudentModel.objects.all()
    context={"student_data":all_data}
    return render(request,'student.html',context)