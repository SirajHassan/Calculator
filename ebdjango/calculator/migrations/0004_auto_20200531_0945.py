# Generated by Django 2.1.1 on 2020-05-31 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_auto_20200531_0740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calculation',
            old_name='calculation',
            new_name='calc_input',
        ),
        migrations.AlterField(
            model_name='calculation',
            name='time',
            field=models.DecimalField(decimal_places=0, default=1590918330.05835, max_digits=10000000000000),
        ),
    ]