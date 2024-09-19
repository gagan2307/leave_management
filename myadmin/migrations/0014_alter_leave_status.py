# Generated by Django 4.2.6 on 2023-10-20 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0013_delete_add_leave_type_remove_leavetype_empid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Declined')], default='Pending', max_length=10),
        ),
    ]