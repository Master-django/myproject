# Generated by Django 3.2.25 on 2024-03-06 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('address', models.CharField(max_length=100, verbose_name='Suroga')),
                ('number_phone', models.IntegerField(verbose_name='Raqami telefon')),
                ('burth_day', models.DateField(verbose_name='soli tavalud')),
                ('nation', models.CharField(max_length=100, verbose_name='Millat')),
            ],
            options={
                'verbose_name': 'Груп',
                'verbose_name_plural': 'групы',
                'db_table': '',
                'managed': True,
            },
        ),
    ]