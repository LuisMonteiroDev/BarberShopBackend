# Generated by Django 4.2.3 on 2023-07-24 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_userprofile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='type',
            field=models.CharField(choices=[('cliente', 'Cliente'), ('barbeiro', 'Barbeiro'), ('desenvolvedor_dono', 'Desenvolvedor dono')], default='', max_length=50, verbose_name='Tipo do usuário'),
        ),
    ]
