from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm


def home(request):
    """"""
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save(**data)
            user = authenticate(username=data['username'], password=data['password1'])
            if user:
                login(request, user)
            return HttpResponseRedirect('/')

    else:
        form = RegistrationForm()
    ctx = {'form': form}

    return render(request, 'register.html', ctx)
