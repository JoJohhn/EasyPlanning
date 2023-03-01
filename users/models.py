from django.db import models
from django.contrib.auth.models import User
from tgbotapp.models import TgUserIds

# Create your models here.

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tgUser = models.ForeignKey(TgUserIds, on_delete=models.CASCADE)