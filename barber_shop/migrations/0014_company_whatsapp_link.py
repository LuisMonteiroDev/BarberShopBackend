# Generated by Django 4.2.3 on 2023-07-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber_shop', '0013_alter_days_hours_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='whatsapp_link',
            field=models.URLField(default=1, max_length=250, verbose_name='Link do Whatsapp'),
            preserve_default=False,
        ),
    ]
