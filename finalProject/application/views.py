from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User

from django.contrib import messages

from .models import Todo


def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_task = Todo(user=request.user, name=task)
        new_task.save()

    existing_todos = Todo.objects.filter(user=request.user)
    context = {
        'todos': existing_todos
    }

    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 5:
            messages.error(request, 'Password is too short. The password must be at least 5 characters long.')
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


def delete_task(request, task_name):
    todo = Todo.objects.get(user=request.user, name=task_name)
    todo.delete()
    return redirect('home')


def update_task(request, task_name):
    todo = Todo.objects.get(user=request.user, name=task_name)
    todo.status = True
    todo.save()
    return redirect('home')


def print_users_tasks(request):
    if request.method == 'POST':
        users_with_todos = []
        users = User.objects.prefetch_related('todo_set').all()

        for user in users:
            todos = user.todo_set.all()
            users_with_todos.append({'user': user, 'todos': todos})

        context = {
            'users_with_todos': users_with_todos
        }

        return render(request, 'users_todos.html', context)

    return render(request, 'users_todos.html')


def deleted_tasks(request):
    pass


def in_progress_tasks(request):
    pass


def completed_tasks(request):
    pass