from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import MyUser



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        # model = MyUser
        fields = {'username', 'password1', 'password2', 'myuser-0-tgUser'}
        # fields = {'myuser-0-tgUser'}
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-input'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        #     'myuser-0-tgUser': forms.TextInput(attrs={'class': 'form-input'}),
        # }