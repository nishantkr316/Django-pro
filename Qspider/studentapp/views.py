from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student_view(request):
    student_data={
        'name':'Nishant Raj Kashyap',
        'address':'Vrindavavn Colony',
        'mob':7903551559,
        'state':'Bihar',
        'city':'patna'
    }
    return render(request,'studentapp/stview.html',student_data)
