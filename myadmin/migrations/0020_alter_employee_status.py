# Generated by Django 4.2.6 on 2023-10-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0019_employee_postingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[(0, 'Active'), (1, 'Inactive')], default='Active', max_length=10),
        ),
    ]