from django.shortcuts import render,redirect
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


from django.db.models import Q
def allarticle_view(request):
    alldata=ArticleModle.objects.all()
    query=request.GET.get('q')

    if query:
        alldata=alldata.filter(
           Q(title__icontains=query)|
           Q(author__icontains=query)|
           Q(description__icontains=query)
        )
    print(query)
    return render(request,'all_articles.html',{'details':alldata})

def spc_article_view(request,id):
    data=ArticleModle.objects.get(id = id)
    return render(request,'spec_art.html',{'data':data})

def delarticle_view(request,id):
     article=ArticleModle.objects.get(id=id)
     if request.method=='POST':
        article.delete()
        return redirect('all_article')
     return render(request,'del_article.html')

def update_view(request ,id):
    data=ArticleModle.objects.get(id=id)
    if request.method=='POST':
        data.title=request.POST.get('title')
        data.description=request.POST.get('description')
        data.author=request.POST.get('author')
        data.date=request.POST.get('date')
        data.save()
        return redirect('spc_art',id=data.id)
    return render(request,'up_article.html',{'data':data})

def del_all_art_view(request):
    if request.method=='POST':
        ArticleModle.objects.all().delete()
        return redirect('all_article')
    return render(request,'del_all_art.html')

