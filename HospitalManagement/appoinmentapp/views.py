from pydoc import doc
from django.shortcuts import render,redirect
from appoinmentapp.models import Doctor,Patient,Appoinment

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def doctor_view(request):
    all=Doctor.objects.all()
    return render(request,'doctor.html',{'all':all})

def patient_view(request):
    all=Patient.objects.all()
    return render(request,'patient.html',{'all':all})

def appoinment_view(request):
    all=Appoinment.objects.all()
    return render(request,'appoinment.html')

def doc_appoinment_view(request,id):
    doc=Doctor.objects.prefetch_related('appoinments').get(id=id)
    #all=doc.appoinments.all()
    return render(request,'docappoinment.html',{'doc':doc})

def pat_appoinment_view(request,id):
    pat=Patient.objects.get(id=id)
    #all=pat.appoinments.all()
    return render(request,'patappoinment.html',{'pat':pat})

             