from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def register(req):
    if req.method == 'POST':
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()  # save the form in the database
            username = form.cleaned_data.get('username')
            messages.success(req, f'account created for {username}!')
            return redirect('store-home')
    else:
        form = UserRegisterForm()
    return render(req, 'users/register.html', {'form': form})
