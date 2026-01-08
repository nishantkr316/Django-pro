from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request,'newsapp/home.html')


def bussiness_view(request):
    h1= "RATAN TATA"
    h2 = "Indian industrialist and former chairperson of the Tata Group"
    h3 = "Ratan Naval Tata [a] (28 December 1937 – 9 October 2024) was an Indian industrialist and philanthropist. He served as the chairman of Tata Group and Tata"

    type = 'business'
    my_dict ={
        'type':type,
        'h1':h1,
        'h2':h2,
        'h3':h3
        }

    return render(request,'newsapp/news.html',context=my_dict)


def sports_view(request):
    h1 = "Cristiano Ronaldo"
    h2 = "Cristiano Ronaldo dos Santos Aveiro is a Portuguese professional footballer"
    h3 = "Football superstar Cristiano Ronaldo ne ab officially keh diya hai ki woh Saudi Arabia ko hi apna permanent ghar bana rahe hain."
    type = 'sports'
    my_dict ={
        'type':type,
        'h1':h1,
        'h2':h2,
        'h3':h3
        }

    return render(request,'newsapp/news.html',context=my_dict)


def entertainment_view(request):
    h1 = "ARIJIT SINGH"
    h2 = "Indian playback singer and composer"
    h3 = "Arijit Singh is an Indian playback singer, composer, music producer and instrumentalist"
    type = 'entertainment'
    my_dict ={
        'type':type,
        'h1':h1,
        'h2':h2,
        'h3':h3
        }


    return render(request,'newsapp/news.html',context=my_dict)
