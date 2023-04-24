from django import forms
from .models import Post, Oblast, House, City


class CreateOblastForm(forms.ModelForm):
    class Meta:
        model = Oblast
        fields = ['oblast']
        widgets = {
            'oblast': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter region'}),
        }


class CreateHouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['address', 'region', 'street', 'flat']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter house address'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter region'}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter street'}),
            'flat':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter flat'}),
        }


class CreateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'})
        }


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter posts title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type something...'})
        }