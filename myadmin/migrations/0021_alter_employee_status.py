# Generated by Django 4.2.6 on 2023-10-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0020_alter_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10),
        ),
    ]
