# Generated by Django 3.0.2 on 2021-04-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_business_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
