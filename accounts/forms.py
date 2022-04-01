from django import forms
from django.contrib.auth import authenticate
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, label='Email')
    password = forms.CharField(label='Parol', widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email,password=password)
            if not user:
                raise forms.ValidationError('Wrong')
        return super(LoginForm, self).clean()