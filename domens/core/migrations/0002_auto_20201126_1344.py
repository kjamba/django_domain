# Generated by Django 3.1.3 on 2020-11-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domens',
            options={'verbose_name': 'Домен', 'verbose_name_plural': 'Домены'},
        ),
        migrations.AlterField(
            model_name='domens',
            name='webserver',
            field=models.CharField(choices=[('nginx', 'nginx'), ('apache2', 'apache2')], max_length=7, verbose_name='Сервер'),
        ),
    ]
