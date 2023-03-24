from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from plannerapp.forms import AddedTask
from plannerapp.models import Task
from django.contrib.auth.models import User


def index_page(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')


@login_required
def tasks_view(request):
    top_level_tasks = Task.objects.filter(taskParent=None, userId=request.user)
    return render(request, 'tasks.html', {'top_level_tasks': top_level_tasks})


@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    data = {'task_name': task.taskName,
            'task_description': task.task,
            'task_parent': task.taskParent,
            'task_start_time': format(task.taskStartTime, '%Y-%m-%dT%H:%M')}

    descendants = task.get_descendants()
    descendants.append(task)
    descendants_id = [descendant.id for descendant in descendants]

    if request.method == "POST":
        form = AddedTask(request.POST, user_id=request.user.id, descendants_id=descendants_id)
        if form.is_valid():
            form.update(task)
            return redirect('tasks')
    else:
        form = AddedTask(user_id=request.user.id, descendants_id=descendants_id, initial=data)
    return render(request, 'edit_task.html', {'form': form})


@login_required
def add_task(request):
    if request.method == "POST":
        form = AddedTask(request.POST, user_id=request.user.id)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            form.save(user)
            return redirect('tasks')
    else:
        form = AddedTask(user_id=request.user.id)
    return render(request, 'add_task.html', {'form': form})