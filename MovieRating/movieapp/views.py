from django.shortcuts import render,redirect
from movieapp.forms import MovieForm,LoginForm,SignupForm
from movieapp.models import MovieModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages




# Create your views here.
def home_view(request):
    type = 'Home'
    return render(request, "base.html",{'type':type})


@login_required
def mov_home_view(request):
    type='Mhome'
    return render(request,'mhome.html',{'type':type})


@login_required
def movie_form(request):
    form=MovieForm()
    if request.method == 'POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies')
    return render(request,'form.html',{'form':form})


@login_required
def all_movies(request):
    movies=MovieModel.objects.all()
    return render(request,'movies.html',{'movies':movies})


@login_required
def del_movie(request,id):
    movie=MovieModel.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies') 
    return render(request,'delete.html')




@login_required
def update_movie(request,id):
    movie= MovieModel.objects.get(id=id)
    form = MovieForm(instance = movie)
    if request.method == 'POST':
        form =MovieForm(request.POST,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies') 
    return render(request,'update.html',{'form':form})

def signup_view(request):
    type='Sign Up'
    form=SignupForm()
    
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request,"User is created Sucessfully...")
            return redirect("login")
    return render(request, "signup.html",{'form':form,'type':type})


def login_view(request):
    type='Login'
    form=LoginForm()
    
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]  
            user=authenticate(username=username,password=password)
            
        if user:
            login(request,user)
            messages.success(request,"Logged in Sucessfully")
            return redirect("mhome")
        
        else:
            messages.warning(request,"Invalid credential...")
    return render(request, "login.html",{'form':form,'type':type})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully...")
    return redirect('login')