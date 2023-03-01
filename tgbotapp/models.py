from django.db import models



class TgUserIds(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, null=True, unique=True)