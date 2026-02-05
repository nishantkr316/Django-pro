from django.shortcuts import render,redirect
from blogapp.models import BlogModel

# Create your views here.
def home_view(request):
    return render(request,'home.html')


def addblog_view(request):
    submitted=False
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        author=request.POST.get('author')
        date=request.POST.get('date')
        BlogModel.objects.create(title=title,description=description,author=author,date=date)
        submitted=True
    return render(request,'addblog.html',{'submitted':submitted})



from django.db.models import Q
def allblog_view(request):
    alldata=BlogModel.objects.all()
    query=request.GET.get('q')
    if query:
        alldata=alldata.filter(
            Q(title__icontains=query)|
           Q(author__icontains=query)|
           Q(description__icontains=query)
        )
    print(query)
    return render(request,'allblog.html',{'details':alldata})



def filterblog_view(request,id):
    data=BlogModel.objects.get(id = id)
    return render(request,'filterblog.html',{'data':data})



def updateblog_view(request ,id):
    data=BlogModel.objects.get(id=id)
    if request.method == 'POST':
        data.title=request.POST.get('title')
        data.description=request.POST.get('description')
        data.author=request.POST.get('author')
        data.date=request.POST.get('date')
        data.save()
        return redirect('filtblog',id=data.id)
    return render(request,'updateblog.html',{'data':data})



def delblog_view(request,id):
    blog=BlogModel.objects.get(id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('allblog')
    return render(request,'delblog.html')



def delallblog_view(request):
    if request.method == 'POST':
        BlogModel.objects.all().delete()
        return redirect('allblog')
    return render(request,'del_all_blog.html')
