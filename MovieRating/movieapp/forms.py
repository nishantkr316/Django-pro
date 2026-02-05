from django import forms
from movieapp.models import MovieModel
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = '__all__'
        widgets = {
            'releasedate':forms.DateInput(attrs={'type':'date'})
        }

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']
        help_texts ={'username':None}

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Exists.....")
        return email
        
class LoginForm(forms.Form):
    username =forms.CharField(max_length=50)
    password =forms.CharField(widget=forms.PasswordInput)