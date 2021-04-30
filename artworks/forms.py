from django import forms
from .models import Artwork, Category


#choices =[('Canvas','Canvas'), ('Mural','Mural'), ('Miscellaneous','Miscellaneous'),]
choices = Category.objects.all().values_list('name','name')
choice_list= []
for item in choices:
    choice_list.append(item)

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields =('title' , 'title_tag', 'author', 'category', 'body' ,'snippet')
        #fields =('title' , 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a cool title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),

            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'userIDauthor', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),

            #'category': forms.Select(attrs={'class': 'form-control'}),
            #'category': forms.Select(choices=choices,attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),


        }


class EditArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields =('title' , 'title_tag', 'category', 'body')
        #fields =('title' , 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is a placeholder'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }