from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import ShopUserLoginForm, ShopUserRegistrationForm


def shop_user_login(request):
    if request.method == "POST":
        login_form = ShopUserLoginForm(data=request.POST)

        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])

            if user:
                login(request, user)
                return redirect('mainapp:main_page')
        else:
            messages.error(request, 'Invalid username or password')
            render(request, 'login_form.html',
                   context={'login_form': ShopUserLoginForm(data=request.POST)})

    return render(request, 'login_form.html', context={'login_form': ShopUserLoginForm()})


def shop_user_logout(request):
    logout(request)
    return redirect('mainapp:main_page')


def shop_user_register(request):
    if request.method == 'POST':
        registration_form = ShopUserRegistrationForm(data=request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)
            return redirect('mainapp:main_page')
        else:
            return render(request, 'registration_form.html', context={'registration_form': registration_form})

    return render(request, 'registration_form.html', context={'registration_form': ShopUserRegistrationForm()})
