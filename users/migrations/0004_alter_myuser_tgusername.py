# Generated by Django 4.1.6 on 2023-02-28 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tgbotapp', '0003_alter_tguserids_name'),
        ('users', '0003_remove_myuser_telegramuserid_myuser_tgusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='tgUserName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tgbotapp.tguserids'),
        ),
    ]
