from django.shortcuts import render
from feedbackapp.models import FeedbackModel

# Create your views here.
def form_view(request):
    submitted = False
    if request.method =='POST':
        a = request.POST['name']
        b = request.POST.get('feedback')
        FeedbackModel.objects.create(name = a, feed = b)
        submitted = True
    return render(request,'form.html',{'submitted':submitted})


def feedback_view(request):
    all_data=FeedbackModel.objects.all()
    return render(request,'feedback.html',{"feedback_data":all_data})