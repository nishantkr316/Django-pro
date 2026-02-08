from django.shortcuts import render,redirect
from blogapp.models import BlogModel
#---Auth----
from blogapp.forms import LoginForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def home_view(request):
    type='Home'
    return render(request,'bhome.html')

@login_required
def addblog_view(request):
    submitted=False
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        bloger=request.POST.get('bloger')
        date=request.POST.get('date')
        BlogModel.objects.create(title=title,description=description,bloger=bloger,date=date)
        submitted=True
    return render(request,'addblog.html',{'submitted':submitted})



from django.db.models import Q
@login_required
def allblog_view(request):
    alldata=BlogModel.objects.all()
    query=request.GET.get('q')
    if query:
        alldata=alldata.filter(
            Q(title__icontains=query)|
           Q(bloger__icontains=query)|
           Q(description__icontains=query)
        )
    print(query)
    return render(request,'allblog.html',{'details':alldata})


@login_required
def filterblog_view(request,id):
    data=BlogModel.objects.get(id = id)
    return render(request,'filterblog.html',{'data':data})


@login_required
def updateblog_view(request ,id):
    data=BlogModel.objects.get(id=id)
    if request.method == 'POST':
        data.title=request.POST.get('title')
        data.description=request.POST.get('description')
        data.bloger=request.POST.get('bloger')
        data.date=request.POST.get('date')
        data.save()
        return redirect('filtblog',id=data.id)
    return render(request,'updateblog.html',{'data':data})


@login_required
def delblog_view(request,id):
    blog=BlogModel.objects.get(id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('allblog')
    return render(request,'delblog.html')


@login_required
def delallblog_view(request):
    if request.method == 'POST':
        BlogModel.objects.all().delete()
        return redirect('allblog')
    return render(request,'del_all_blog.html')




def signup_view(request):
    form=SignupForm()
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request,"Account created successfully...")
            return redirect("login")
    return render(request, "signup.html",{'form':form})




def login_view(request):
    form=LoginForm()
    
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]  
            user=authenticate(username=username,password=password)
            
        if user:
            login(request,user)
            messages.success(request,"Logged in successfully...")
            return redirect("home")
        
        else:
            messages.warning(request,"Invalid username or password...")
    return render(request, "login.html",{'form':form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully...")
    return redirect('login')


from django.contrib.auth.forms import PasswordChangeForm
@login_required
def new_password(request):
    form =PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Password changed successfully...")
            return redirect('home')
    return render(request, "new_password.html", {'form': form})