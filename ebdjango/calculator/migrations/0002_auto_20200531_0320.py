# Generated by Django 2.1.1 on 2020-05-31 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculation',
            name='time',
            field=models.DecimalField(decimal_places=0, default=1590895223.5318432, max_digits=10000000000000),
        ),
        migrations.AlterField(
            model_name='calculation',
            name='result',
            field=models.CharField(max_length=120),
        ),
    ]
