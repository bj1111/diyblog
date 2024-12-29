from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, PasswordResetForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_register(request):
    """ User registration """
    
    # Check that users cannot access the registration page if they are already authenticated
    if request.user.is_authenticated:
        messages.error(request, "You don't have access to this page. ", 'danger')
        return redirect('blog:index')
        
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password1'],
                first_name=data['firstname'],
                last_name=data['lastname'],
                email=data['email'],
            )
            if user:
                messages.success(request, "User created successfully.")
                return redirect('accounts:login')
            
            else:
                messages.error(request, "Can't be signed in.", 'danger')
                
        return render(request, 'accounts/register.html', {'form':form})
    
    else:
        form = RegisterForm
        return render(request, 'accounts/register.html', {'form':form})

def user_login(request):
    """ User login """
    
    # Check that users cannot access the login page if they are already authenticated
    if request.user.is_authenticated:
        messages.error(request, "You don't have access to this page. ", 'danger')
        return redirect('blog:index')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "User logged in successfully.")
                return redirect('blog:index')
            
            else:
                messages.error(request, "Username or password is wrong. ", 'danger')
                
        return render(request, 'accounts/login.html', {'form':form})
            
    else:
        form = LoginForm
        return render(request, 'accounts/login.html', {'form':form})

@login_required(login_url='accounts:login')
def user_logout(request):
    """ User logout """
    logout(request)
    messages.success(request, "User logged out successfully.")
    return redirect('blog:index')

@login_required(login_url='accounts:login')
def user_info(request,user_id):
    """ User information """
    user_info = get_object_or_404(User,username=user_id)
    return render(request, 'accounts/user_info.html', {'user_info':user_info})

@login_required(login_url='accounts:login')
def reset_password(request, user_id):
    """View to reset password using username from the URL"""
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            # Validate old password
            if not user.check_password(cleaned_data['old_password']):
                messages.error(request, "Current password is incorrect.")
                return render(request, 'accounts/reset_password.html', {'form': form})

            # Update password
            user.set_password(cleaned_data['new_password'])
            user.save()
            messages.success(request, "Password reset successfully. Please log in again.")
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/reset_password.html', {'form': form})

    # Pre-fill form without asking for username
    form = PasswordResetForm()
    return render(request, 'accounts/reset_password.html', {'form': form})
