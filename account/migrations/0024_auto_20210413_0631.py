# Generated by Django 3.0.2 on 2021-04-13 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_auto_20210413_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]