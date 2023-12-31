# Generated by Django 4.2.3 on 2023-08-16 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barber_shop', '0018_alter_days_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='days',
            name='end_pause_time',
            field=models.TimeField(blank=True, help_text='(opcional)', null=True, verbose_name='Fim da pausa'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='barbershop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='barber_shop.company', verbose_name='Barbearia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedules',
            name='day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='schedules_days', to='barber_shop.days', verbose_name='Dia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schedules',
            name='user_canceled',
            field=models.BooleanField(default=False, verbose_name='Cancelado pelo usuário?'),
        ),
        migrations.AlterField(
            model_name='company',
            name='whatsapp_link',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='Link do whatsapp'),
        ),
        migrations.AlterField(
            model_name='days',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_dat', to='barber_shop.company', verbose_name='Barbearia'),
        ),
        migrations.AlterField(
            model_name='days',
            name='pause_time',
            field=models.TimeField(blank=True, help_text='(opcional)', null=True, verbose_name='Horário de pausa'),
        ),
        migrations.CreateModel(
            name='SchedulesDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedule_day', to='barber_shop.days', verbose_name='Dia')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedule', to='barber_shop.schedules', verbose_name='Agendado por')),
            ],
            options={
                'verbose_name': 'Dia agendado',
                'verbose_name_plural': 'Dias agendados',
            },
        ),
    ]
