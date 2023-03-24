from django import forms
from plannerapp.models import Task


class AddedTask(forms.Form):

    task_name = forms.CharField(label='Название задачи',
                                widget=forms.TextInput(attrs={'class': 'form-input'}))
    task_description = forms.CharField(label='Описание задачи',
                                       widget=forms.TextInput(attrs={'class': 'form-input'}),
                                       required=False)
    task_parent = forms.ModelChoiceField(label='Задача родитель',
                                         widget=forms.Select(attrs={'class': 'form-input'}),
                                         queryset=None,
                                         to_field_name='taskName',
                                         required=False)
    task_start_time = forms.DateTimeField(label='Дата и время начала задачи',
                                          input_formats=['%Y-%m-%dT%H:%M'],
                                          widget=forms.DateTimeInput(attrs={'class': 'form-input',
                                                                            'type': 'datetime-local'}))

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        descendants_id = kwargs.pop('descendants_id', [])
        super(AddedTask, self).__init__(*args, **kwargs)
        self.fields['task_parent'].queryset = Task.objects.filter(userId=user_id).exclude(id__in=descendants_id)

    def update(self, task):
        form_data = self.cleaned_data
        task.taskName = form_data['task_name']
        task.task = form_data['task_description']
        task.taskParent = form_data['task_parent']
        task.taskStartTime = form_data['task_start_time']
        task.save()

    def save(self, user):
        form_data = self.cleaned_data
        task = Task.objects.create(taskName=form_data['task_name'],
                                   task=form_data['task_description'],
                                   taskParent=form_data['task_parent'],
                                   userId=user,
                                   taskStartTime=form_data['task_start_time'])
        task.save()

