from django.shortcuts import render, redirect
from django.views import View
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from . import forms 



class UserRegisterView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account:profile')
        return super().dispatch(request, *args, **kwargs)
    
    form_class = forms.UserRegisterForm
    template = 'account/register.html'

    def get(self, request):
        register_form = self.form_class()
        return render(request, self.template, {'form': register_form})
    
    def post(self, request):  
        register_form = self.form_class(request.POST)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request,'ثبت شد' ,'success')
            return redirect('account:profile')
        
        return render(request, self.template, {'form': register_form})



class UserLoginView(View):
    #This function is for user verification so that a user who has logged in cannot log in again; 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account:profile')
        return super().dispatch(request, *args, **kwargs)
    
    form_class = forms.UserLoginForm
    template = 'account/login.html'
    
    def get(self, request):
        login_form = self.form_class()
        return render(request, self.template, {'form': login_form})

    def post(self, request):
        login_form = self.form_class(request.POST)

        if login_form.is_valid():
            clear_data = login_form.cleaned_data
            user = authenticate(request, username=clear_data['username'], password=clear_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'your login is successfully', 'success')
                return redirect('account:profile')
            messages.error(request, 'username or password is wrong !', 'worning')

        return render(request, self.template, {'form': login_form})



class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'your logout is successfully', 'success')
        return redirect('account:profile')



class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user_id = request.user.id 
        user = User.objects.get(pk=user_id)
        return render(request, 'account/profile.html', {'object': user})
    