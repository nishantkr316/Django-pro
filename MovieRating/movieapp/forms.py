from django import forms
from movieapp.models import MovieModel

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = '__all__'
        widgets = {
            'releasedate':forms.DateInput(attrs={'type':'date'})
        }