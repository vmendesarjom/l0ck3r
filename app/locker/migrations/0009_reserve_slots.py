# Generated by Django 2.0.7 on 2018-08-14 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0008_auto_20180814_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='slots',
            field=models.ManyToManyField(to='locker.Slot', verbose_name='Slot'),
        ),
    ]
