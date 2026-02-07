from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']
        help_texts ={'username':None}

# Only unique And gmail domain allowed

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Exists.....")
        elif  not email.lower().endswith('@gmail.com'):
            raise forms.ValidationError("Only gmail is allowed")
        return email
    

# Username at least 5 charcters

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username)<5:
            raise forms.ValidationError("Username must be at least 5 characters")
        return username
    


# PAssword At least 8 char include num ,char ,special symbol 
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError("Password must be at least 8 characters")
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must contain at least one number")
        if not any(char.isalpha() for char in password):
            raise forms.ValidationError("Password must contain at least one letter")
        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/' for char in password):
            raise forms.ValidationError("Password must contain at least one special character")
        return password
    




    # def clean_password(self):
    #     import re
    #     password =self.cleaned_data['password']
    #     if (
    #         len(password)< 8 or
    #         not (re.search("\d",password)) or 
    #         not(re.search("[A-Za-z]",password)) or 
    #         not(re.search("\W",password))
    #     ):
    #         raise forms.ValidationError("password must be 8 char"
    #                                     "must contain 1 uppercase"
    #                                     "must contain digit and special symbol")
    #     return password

        
        
class LoginForm(forms.Form):
    username =forms.CharField(max_length=50)
    password =forms.CharField(widget=forms.PasswordInput)





