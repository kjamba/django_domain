# Generated by Django 3.1.3 on 2020-11-19 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webserver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Веб сервер',
                'verbose_name_plural': 'Веб серверы',
            },
        ),
        migrations.CreateModel(
            name='Domens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Название')),
                ('status', models.BooleanField(default=False, verbose_name='Cтатус')),
                ('webserver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.webserver', verbose_name='Веб сервер')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
    ]
