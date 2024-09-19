# Generated by Django 4.2.6 on 2023-11-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0040_alter_leave_fromdate_alter_leave_todate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Declined')], default='Approved', max_length=10),
        ),
    ]
