from django import forms
from .models import Blog, Post, House, City


class CreateBlogForm(forms.ModelForm):
    house_address = forms.CharField(required=True,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control', 'placeholder': 'Enter house address'}))
    oblast = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Enter region'}))

    city = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Enter city'}))

    class Meta:
        model = Blog
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter blog description'}),

        }


class CreatePostForm(forms.ModelForm):
    house_address = forms.CharField(required=True,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control', 'placeholder': 'Enter house address'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'blog']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type something...'}),
            'blog': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        house_address = cleaned_data.get("house_address")

        if not house_address:
            raise forms.ValidationError("Please enter a valid house address.")

        try:
            house = House.objects.get(address=house_address)
        except House.DoesNotExist:
            raise forms.ValidationError("The entered house address does not exist.")

        cleaned_data['house'] = house
        return cleaned_data


