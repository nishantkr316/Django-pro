from django.shortcuts import render
from myapp.forms import ContactForm,StudentForm

# Create your views here.
def contact_view(request):
    form = ContactForm()
    return render(request, 'contact.html',{"form":form})




def student_view(request):
    form=StudentForm()
    return render(request, 'student.html',{"form":form})
