from django.shortcuts import render
from myapp.models import EmployeeModel

# Create your views here.
def employee_View(request):
    all_data=EmployeeModel.objects.all()
    context={"employee_data":all_data}
    return render(request,'employee.html',context)

