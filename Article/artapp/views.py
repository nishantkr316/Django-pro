from django.shortcuts import render,redirect
from artapp.models import ArticleModel
from artapp.forms import ArticleForm, SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required
def home_view(request):
    return render(request, 'home.html')


@login_required
def article_create(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articles')
    return render(request, 'addart.html', {'form': form}) 




from django.db.models import Q
@login_required
def allarticle_list(request):
    articles=ArticleModel.objects.all()
    q = request.GET.get('q')
    if q:
        articles = articles.filter(Q(title__icontains=q) | Q(content__icontains=q) | Q(author__icontains=q))
    return render(request, 'allart.html', {'articles': articles})


@login_required
def filter_article(request, id):
    article = ArticleModel.objects.get(id=id)
    return render(request, 'filart.html', {'article':article})


@login_required
def article_update(request, id):
    article=ArticleModel.objects.get(id=id)
    form=ArticleForm(instance=article)
    if request.method == 'POST':
        form=ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
    return render(request, 'upart.html', {'form': form})  


@login_required
def delete_article(request,id):
    movie=ArticleModel.objects.get(id=id)
    if request.method=='POST':          
        movie.delete()
        return redirect('articles')
    return render(request, 'delart.html')

def delall_article(request):
    articles=ArticleModel.objects.all()
    if request.method=='POST':
        articles.delete()
        return redirect('articles')
    return render(request, 'delallart.html')



#------auth-----------


def signup_view(request):
    type='Sign Up'
    form=SignupForm()
    
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request,"Account created successfully...")
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
            messages.success(request,"Logged in successfully...")
            return redirect("home")
        
        else:
            messages.warning(request,"Invalid username or password...")
    return render(request, "login.html",{'form':form,'type':type})


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
