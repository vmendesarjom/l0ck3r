# Generated by Django 2.0.7 on 2018-08-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0004_auto_20180811_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projector',
            name='type',
            field=models.CharField(choices=[('Interativo', 'Computador Interativo'), ('DataShow', 'Datashow')], default='DataShow', max_length=10, verbose_name='Tipo'),
        ),
    ]
