# Generated by Django 4.2.6 on 2023-10-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0015_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='empcode',
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
