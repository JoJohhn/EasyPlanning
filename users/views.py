from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from users.forms import MyUserCreationForm, MyUserLoginForm
from users.models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView


def register_user(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            tgUsername = form.cleaned_data.get('tgUsername')
            user = User.objects.get(username=username)
            user_data = MyUser.objects.create(user=user, tgUser=tgUsername)
            user_data.save()
            return redirect('login')
    else:
        form = MyUserCreationForm()
    return render(request, 'register.html', {'form':form})


class LoginUser(LoginView):
    template_name = 'login.html'
    form_class = MyUserLoginForm
    # redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
