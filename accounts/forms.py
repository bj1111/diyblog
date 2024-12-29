from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password


class RegisterForm(forms.Form):
    """ A form to create a user """
    firstname = forms.CharField(
        label='First Name:',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'First Name'}
        )
    )
    lastname = forms.CharField(
        label='Last Name:',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Last Name'}
        )
    )
    email = forms.EmailField(
        label='Email:',
        widget=forms.EmailInput(
            attrs={'class':'form-control', 'placeholder':'Email'}
        )
    )
    username = forms.CharField(
        label='Username:',
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'Username'}
        )
    )
    password1 = forms.CharField(
        label='Password:',
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Password'}
        )
    )
    password2 = forms.CharField(
        label='Confirmation password:',
        widget=forms.PasswordInput(
            attrs={'class':'form-control', 'placeholder':'Confirmation password'}
        )
    )

    # Check for unique user
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("Username is already exists. ")
        
        return username
        
    # Validate two fields
    def clean(self):
        data = super().clean()
        p1 = data.get('password1')
        p2 = data.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError("Passwords don't match. ")

class LoginForm(forms.Form):
    """ User login form """
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        )
    )

class PasswordResetForm(forms.Form):
    """Form for resetting the password directly"""
    old_password = forms.CharField(
        label="Current Password:",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Current Password'}
        )
    )
    new_password = forms.CharField(
        label="New Password:",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'New Password'}
        )
    )
    confirm_password = forms.CharField(
        label="Confirm New Password:",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:
            raise forms.ValidationError("New passwords do not match.")

        return cleaned_data




