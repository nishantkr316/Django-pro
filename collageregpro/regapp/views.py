from django.shortcuts import render
from regapp.models import StudentModel
# Create your views here.
def form_view(request):
    submitted=False
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobno=request.POST.get('mobno')
        sub=request.POST.get('sub')
        city=request.POST.get('city')
        add=request.POST.get('add')
        StudentModel.objects.create(name=name,email=email,mobno=mobno,sub=sub,city=city,add=add)
        submitted=True
    return render(request,'form.html',{'submitted':submitted})


def studentdata_view(request):
    alldata=StudentModel.objects.all()
    return render(request,'student-data.html',{'details':alldata})
