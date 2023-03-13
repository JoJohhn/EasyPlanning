from django.shortcuts import render, redirect
from plannerapp.forms import AddedTask
from plannerapp.models import Task


def index_page(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')



def tasks_view(request):
    top_level_tasks = Task.objects.filter(taskParent=None, userId=request.user)
    return render(request, 'tasks.html', {'top_level_tasks': top_level_tasks})


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    print(task.task)
    data = {'task_name': task.taskName,
            'task_description': task.task}
    if request.method == "POST":
        form = AddedTask(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            task.taskName = form_data['task_name']
            task.save()
            return redirect('tasks')
    else:
        form = AddedTask(data)

    return render(request, 'edit_task.html', {'form': form})

