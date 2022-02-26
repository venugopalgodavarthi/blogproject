from cmath import log
from django.http import HttpResponse
from django.shortcuts import redirect, render
from authe.forms import registerform, loginform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def registerview(request):
    form = registerform()
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
    return render(request, 'register.html', {'form': form})


def loginview(request):
    form = loginform()
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                print(request.user)
                return redirect('/index')
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/authe/login')
def logoutview(request):
    logout(request)
    return redirect('/authe/login')


@login_required(login_url='/authe/login')
def homeview(request):
    return render(request, 'home.html')
