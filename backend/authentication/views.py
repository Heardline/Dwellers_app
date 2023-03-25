from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User
import random
import string

def generate_temp_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.temp_code = generate_temp_code()
            user.save()
            ''' Для тестов используем временный вариант с html'''
            return render(request, 'authentication/show_temp_code.html', {'temp_code': user.temp_code}) 
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        temp_code = request.POST['temp_code']
        try:
            user = User.objects.get(username=username, secret_hash=temp_code)
            login(request, user)
            return redirect('newsfeed:index')
        except User.DoesNotExist:
            return HttpResponse("Invalid username or temporary code")
    else:
        return render(request, 'authentication/login.html')