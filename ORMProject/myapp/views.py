from django.shortcuts import render
from myapp.models import EmployeeModel
from django.db.models import Q,Max,Min,Avg,Sum,Count

# Create your views here.

def retrive_data(request):
    all_data=EmployeeModel.objects.all()
    context={"employee_data":all_data}
    return render(request,'all_data.html',context)

def fiter_data(request):
    all_data=EmployeeModel.objects.filter(salary=45157)
    all_data=EmployeeModel.objects.filter (Q(id__range=[10,15]) | Q(salary__gt =50000))
    all_data=EmployeeModel.objects.filter(salary__gte = 60000)
    context={"employee_data":all_data}
    return render(request,'filter.html',context)

def aggregate_view(request):
    max=EmployeeModel.objects.aggregate(max_sal=Max('salary'))
    min=EmployeeModel.objects.aggregate(min_sal=Min('salary'))
    avg=EmployeeModel.objects.aggregate(avg_sal=Avg('salary'))
    sum=EmployeeModel.objects.aggregate(sum_sal=Sum('salary'))
    count=EmployeeModel.objects.aggregate(count_sal=Count('salary'))
    context={
        'max':max,
        'min':min,
        'avg':avg,
        'sum':sum,
        'count':count
    }
    return render (request,'aggregate_data.html',context)
