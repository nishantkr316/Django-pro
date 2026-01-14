from django.shortcuts import render
from myapp.models import ArticleModle

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def form_view(request):
    submitted=False
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        author=request.POST.get('author')
        date=request.POST.get('date')
        ArticleModle.objects.create(title=title,description=description,author=author,date=date)
        submitted=True
    return render(request,'form.html',{'submitted':submitted})

def allarticle_view(request):
    alldata=ArticleModle.objects.all()
    return render(request,'all_articles.html',{'details':alldata})

def spc_article_view(request):
    alldata=ArticleModle.objects.filter(id=3)
    return render(request,'spec_art.html',{'details':alldata})
