# Generated by Django 4.2.6 on 2023-11-10 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myadmin', '0044_rename_user_department_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='admin',
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]