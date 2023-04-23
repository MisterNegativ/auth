from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate
from user.forms import UserRegistrationForm, LoginForm, ProfileForm
from user.models import Profile


def login_page(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.data.get('username'), password=form.data.get('password'))
            try:
                profile = Profile.objects.get(owner_id=user.id)
            except:
                profile = Profile(owner_id=user.id)
                profile.save()
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
            user.save()
            profile = Profile(owner_id=user.id)
            profile.save()
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


def settings_page(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            profile = Profile.objects.get(owner_id=request.user.id)
            form = ProfileForm
            return render(request, 'user/profile.html', {'profile': profile, 'form': form})
        if request.method == 'POST':
            pass
    else:
        return redirect('/')

