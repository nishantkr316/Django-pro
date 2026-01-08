from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random

# Create your views here.
def horoscopr_view(request):
    hr=datetime.datetime.now().time().hour
    if hr<12:
        msg =' Morning'
    elif hr <16:
        msg=' Afternoon'
    elif hr<20:
        msg=' Evening'
    else:
        msg=' Night'

    list1=[
        'Golden days ahead',
        'Very soon you will get a job',
        'Spray water to reduce AQI',
        'Watch reels before sleeep',
        'Sleep more even in the class',
        'Better to smoke in home instead going outside',
        'Avoid water drink rum'
    ]

    name_list=['Yash','Nitesh','Sonal','Rublin','saroj','Rahul']
    candidate_list=['shardha','Nora','Samantha','Tamana','kiara','Rashmika']

    s=random.choice(list1)
    name=random.choice(name_list)
    candidate=random.choice(candidate_list)

    my_dict={
        'wish':msg,
        'message':s,
        'name':name,
        'candidate':candidate
    }
    return render(request,'astro.html',my_dict)
def home_view(request):
    return render(request,'home.html')
