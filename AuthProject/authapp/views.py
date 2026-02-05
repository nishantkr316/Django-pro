from django.shortcuts import render,redirect
from authapp.forms import LoginForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def home_view(request):
    type = 'Home'
    return render(request, "home.html",{'type':type}) 







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
            return redirect("home")
        
        else:
            messages.warning(request,"Invalid credential...")
    return render(request, "login.html",{'form':form,'type':type})






@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully...")
    return redirect('login')






def about_view(request):
    type='About'
    return render(request, "about.html",{'type':type})





@login_required
def recent_view(request):
    type='Recent'
    return render(request, "recent.html",{'type':type})