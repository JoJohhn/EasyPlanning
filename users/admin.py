from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import MyUser
# Register your models here.


class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = 'myuser'

class UserAdmin(BaseUserAdmin):
    inlines = (MyUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
