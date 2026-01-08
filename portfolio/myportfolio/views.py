from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def base_view(request):
    return render(request,'base.html')
def home_view(request):
    return render(request,'home.html')
def blog_view(request):
    return render(request,'blog.html')
def about_view(request):
    about_data={
        'name':'Nishant Raj Kashyap',
        'address':'Vrindavavn Colony',
        'mob':7903551559,
        'state':'Bihar',
        'city':'patna'
    }
    return render(request,'about.html',about_data)
def contact_view(request):
    contact_data={
        'mob':7903551559,
        'email':'nraj6014@gmail.com',
    }
    return render(request,'contact.html',contact_data)
