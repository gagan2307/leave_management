# Generated by Django 4.2.6 on 2023-10-20 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0006_leave_leave_type_leave_posting_date_leave_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='city',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='dob',
        ),
    ]
