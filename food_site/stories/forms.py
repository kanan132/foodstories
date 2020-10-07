from .models import Contact, Recipe
from django import forms 

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'id':'firstname','placeholder':'enter name', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'id':'email','placeholder':'enter email', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'id':'subject','placeholder':'enter subject', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'id':'message','placeholder':'enter message', 'class': 'form-control'}),
        }



class CreateStoryForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'short_dscrp','description','image', 'category')


        widgets = {
            'title' : forms.TextInput(attrs={'id': 'title', 'placehoder': 'Enter title', 'class':'form-control'}),
            'short_dscrp' : forms.TextInput(attrs={'id': 'short_dscrp', 'placehoder': 'Short description', 'class':'form-control'}),
            'description' : forms.TextInput(attrs={'id': 'description', 'placehoder': 'Enter description', 'class':'form-control'}),
            'image': forms.FileInput(attrs={'id': 'image', 'placeholder': 'Image', 'class': 'form-control'}),
            'category': forms.Select(attrs={'id': 'category', 'placeholder': 'Category', 'class': 'form-control'}),
        }


