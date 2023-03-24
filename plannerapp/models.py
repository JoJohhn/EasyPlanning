from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    taskName = models.CharField(max_length=255, null=False)
    task = models.TextField(max_length=255, blank=True)
    taskParent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subtasks')
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    taskStartTime = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)


    def __str__(self):
        return f'{self.taskName}'


    def get_descendants(self):
        descendants = []
        for subtask in self.subtasks.all():
            descendants.append(subtask)
            descendants.extend(subtask.get_descendants())
        return descendants