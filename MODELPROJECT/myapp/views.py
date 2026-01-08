from django.shortcuts import render
from myapp.models import Studentmodel

# Create your views here.
def student_View(request):
    all_data=Studentmodel.objects.all()
    context={"student_data":all_data}
    return render(request,'Student.html',context)
    

