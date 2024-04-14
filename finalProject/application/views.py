from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 5:
            messages.error(request, 'Password is too short. It must be at least 5 characters long.')
            return redirect('register')

        users_by_username = User.objects.filter(username=username)
        if users_by_username:
            messages.error(request, 'User with this username already exists.')
            return redirect('register')

        new_user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        new_user.save()

        messages.success(request, 'New user successfully registered. Please proceed to login.')
        return redirect('login')

    return render(request, 'register.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid input or this user does not exist.')
            return redirect('login')

    return render(request, 'login.html')