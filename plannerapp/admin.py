from django.contrib import admin
from plannerapp.models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('taskName', 'taskParent',)

admin.site.register(Task, TaskAdmin)
