from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from plannerapp.models import Task
# Create your views here.


def index_page(request):
    return render(request, 'index.html')

def tasks(request):
    mytasks = Task.objects.all().values()
    template = loader.get_template('all_tasks.html')
    context = {
        'mytasks': mytasks,
    }
    return HttpResponse(template.render(context, request))


def base(request):
    return render(request, 'base.html')