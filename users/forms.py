from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    User Register Form; inherits from Django UserCreationForm. Enables the
    registration form to collect User email data alongside of default inputs.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class UserUpdateForm(forms.ModelForm):
    """
    User Update Form; inherits from Django User Model. Enables the
    user to update their user information.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Profile Update Form; inherits from Profile Model. Enables the
    user to update their profile information.
    """

    class Meta:
        model = Profile
        fields = ['image', 'bio']
