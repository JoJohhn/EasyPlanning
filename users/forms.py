from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tgbotapp.models import TgUserIds




class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    tgUsername = forms.ModelChoiceField(label='Телеграм', widget=forms.TextInput(attrs={'class': 'form-input'}), queryset=TgUserIds.objects.all(), to_field_name='name')
    class Meta():
        model = User
        fields = {'username', 'password1', 'password2', 'tgUsername'}
        # fields = UserCreationForm.Meta.fields
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-input'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        #     'tgUsername': forms.TextInput(attrs={'class': 'form-input'}),
        # }