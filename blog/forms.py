from django import forms
from .models import Blog,Comment

class BlogCreationForm(forms.ModelForm):
    """ A form to create a blog """
    class Meta:
        model = Blog
        fields = ['title', 'text']
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control', 'style': 'height: 300px;'}),
        }
        
class BlogUpdateForm(forms.ModelForm):
    """ A form to update a blog """
    class Meta:
        model = Blog
        fields = ['title', 'text']
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control', 'style': 'height: 300px;'}),
        }

class AddCommentForm(forms.ModelForm):
    """ A form to add a comment """
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Your Comment',
        }
        
    
        widgets = {
            'text' : forms.Textarea(attrs={'class':'form-control', 'style': 'height: 100px; margin-top: 10px;'}),
        }

       
