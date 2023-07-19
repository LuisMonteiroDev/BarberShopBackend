# Generated by Django 4.2.3 on 2023-07-19 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barber_shop', '0007_company_employees_remove_company_owner_company_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedules',
            name='chosen_barber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_chosen_barber', to=settings.AUTH_USER_MODEL, verbose_name='Barbeiro escolhido pelo cliente'),
        ),
    ]
