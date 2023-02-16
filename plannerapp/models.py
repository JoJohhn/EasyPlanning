from django.db import models

# Create your models here.


class Task(models.Model):
    taskName = models.CharField(max_length=255)
    task = models.CharField(max_length=255)