from django.shortcuts import render

# Create your views here.
def form_view(request):
    return render(request,'form.html')
def feedback_view(request):
    return render(request,'feedback.html')