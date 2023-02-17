from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):
    taskName = models.CharField(max_length=255, null=False)
    task = models.TextField(max_length=255, blank=True)
    taskParent = models.IntegerField(null=False)
    userId = models.IntegerField(null=False)
    taskStartTime = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)


    def __str__(self):
        return f'{self.taskName}'