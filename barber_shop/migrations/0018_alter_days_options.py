# Generated by Django 4.2.3 on 2023-07-30 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barber_shop', '0017_days_pause_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='days',
            options={'verbose_name': 'Dia', 'verbose_name_plural': 'Dias de Funcionamento'},
        ),
    ]
