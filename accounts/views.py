from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'account/sign-up.html', {'form': form})