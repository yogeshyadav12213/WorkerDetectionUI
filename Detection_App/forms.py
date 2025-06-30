from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-input', 'placeholder': 'Choose a username'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-input', 'placeholder': 'Choose a strong password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-input', 'placeholder': 'Confirm your password'}
        )
