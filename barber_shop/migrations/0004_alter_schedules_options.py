# Generated by Django 4.2.3 on 2023-07-18 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barber_shop', '0003_schedules'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedules',
            options={'verbose_name': 'Agendamento', 'verbose_name_plural': 'Agendamentos'},
        ),
    ]
