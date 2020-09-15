from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm


def register(request):
    """
    User Registration Form View; allows users to register an account.
    If the request method is POST, the register form will have the POST data.
    Otherwise, the form will be empty.
    """
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('posts-front-page')
    else:
        register_form = UserRegisterForm()

    context = {'register_form': register_form}
    return render(request, 'users/register.html', context)
