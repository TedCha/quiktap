from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm


def register(request):
    """
    User Registration Form View; allows users to register an account.
    If the request method is POST, the register form will have the POST data.
    Otherwise, the form will be empty.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    return render(request, 'users/profile.html')
