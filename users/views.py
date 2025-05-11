from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm
from .models import User, UserManager

# Create your views here.
"""Login view"""
def user_login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email = email, password = password)

            if user is not None and user.check_password(password):
                if user.is_superuser:
                    auth_login(request, user)
                    return redirect('/admin')
                else:
                    auth_login(request, user)
                    messages.success(request, "You are successfully logged in. Enjoy shopping!")
                    return redirect('home')
            else:
                print(form.errors)
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Somehow this form is not valid.')
            print(form.errors)
            return render(request, 'users/login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

"""Register user view"""
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            messages.success(request, "User created successfully.")
            return redirect('users:login')
        else:
            messages.error(request, "Something went wrong. Check you input and try again.")
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})

"""Logout view"""
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('users:login')    

"""View Profile view"""
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html')
    else:
        messages.warning(request, 'You must login to proceed.')
        return redirect("users:login")