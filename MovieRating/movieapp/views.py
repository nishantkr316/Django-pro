from django.shortcuts import render,redirect
from movieapp.forms import MovieForm
from movieapp.models import MovieModel



# Create your views here.
def movie_form(request):
    form=MovieForm()
    if request.method == 'POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies')
    return render(request,'form.html',{'form':form})



def all_movies(request):
    movies=MovieModel.objects.all()
    return render(request,'movies.html',{'movies':movies})



def del_movie(request,id):
    movie=MovieModel.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies') 
    return render(request,'delete.html')



def update_movie(request,id):
    movie= MovieModel.objects.get(id=id)
    form = MovieForm(instance = movie)
    if request.method == 'POST':
        form =MovieForm(request.POST,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies') 
    return render(request,'update.html',{'form':form})