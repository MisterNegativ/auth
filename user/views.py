from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate
from user.forms import UserRegistrationForm, LoginForm


def login_page(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.data.get('username'), password=form.data.get('password'))
            login(request, user)
            if user is not None:
                return redirect('/')
            else:
                form.add_error(field='username', error='Invalid password or login')
                return render(request, 'user/login.html', {'form': form})
        else:
            return render(request, 'user/login.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            auth_data = authenticate(request, email=email, password=password)
            if auth_data is not None:
                login(request, auth_data)
                return redirect('/')
            else:
                return redirect('/auth/login/')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/registration.html', {'form': form})


def logout_page(request):
    auth.logout(request)
    return redirect('/auth/login')
