from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tgbotapp.models import TgUserIds




class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    tgUsername = forms.ModelChoiceField(label='Имя пользователя телеграм',
                                        widget=forms.TextInput(attrs={'class': 'form-input'}),
                                        queryset=TgUserIds.objects.all(),
                                        to_field_name='name',
                                        error_messages={'invalid_choice': 'Вы неправильно ввели имя пользователя телеграм или не активировали бота'})

    field_order = ['username', 'tgUsername', 'password1', 'password2']



class MyUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    field_order = ['username', 'password']