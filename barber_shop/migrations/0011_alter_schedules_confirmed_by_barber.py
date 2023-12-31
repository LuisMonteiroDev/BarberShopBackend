# Generated by Django 4.2.3 on 2023-07-22 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_shop', '0010_alter_company_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='confirmed_by_barber',
            field=models.BooleanField(blank=True, default=False, help_text='Aguarde até o barbeiro confirmar o agendamento', null=True, verbose_name='Agendamento confirmado pelo barbeiro?'),
        ),
    ]
