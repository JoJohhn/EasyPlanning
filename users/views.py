from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from users.forms import MyUserCreationForm
from users.models import MyUser
from django.contrib.auth.models import User


# def register(request):
#     return render(request, 'register.html')


# class RegisterUser(CreateView):
#     form_class = MyUserCreationForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('base')

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
            return redirect('base')
    else:
        form = MyUserCreationForm()
    return render(request, 'register.html', {'form':form})