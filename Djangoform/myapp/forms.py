from django import forms    
from myapp.models import StudentModel


#django forms --you dont have model
class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)





#django model form-- you have model
class StudentForm(forms.ModelForm):
    class Meta: #defining metadata metadata containd data of data
        model = StudentModel
        fields = ['name', 'sub', 'rollno']                                                             