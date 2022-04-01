from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def Login_View(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'form.html', {'form': form})

def Home(request):
    text = "anasehofe --> " + request.user.email
    return HttpResponse(text)

def Logout_view(request):
    logout(request)
    return redirect('login')