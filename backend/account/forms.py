from django import forms
from .models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TelInput(attrs={'class': 'py-3 px-4 w-full rounded-lg mt-4 border border-gray-300 focus:ring-2 focus:ring-green-400'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'py-3 px-4 w-full rounded-lg mt-4 border border-gray-300 focus:ring-2 focus:ring-green-400'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'py-3 px-4 w-full rounded-lg mt-4 border border-gray-300 focus:ring-2 focus:ring-green-400'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'py-3 px-4 w-full rounded-lg mt-4 border border-gray-300 focus:ring-2 focus:ring-green-400'}))


    def clean_username(self):
            username = self.cleaned_data['username']
            user = User.objects.filter(username=username).exists()
            if user:
                raise ValidationError('This Usename be exists')
            return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email be exists')
        return email

    def clean(self):
        clean_data = super().clean()
        p1 = clean_data.get('password')
        p2 = clean_data.get('password2')

        if p1 and p2 and  p1 != p2:
             raise ValidationError('passwords must match..!')


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TelInput(attrs={'class':'py-3 px-2 w-full rounded-2xl mt-4 mx-10'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'py-3 px-2 w-full rounded-2xl mx-10 mt-4'}))