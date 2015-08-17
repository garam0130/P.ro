from django.shortcuts import render, redirect
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login(request):
    return auth_login(request, template_name='registration/login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')

    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html')
