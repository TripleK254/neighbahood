# Generated by Django 3.0.2 on 2021-04-11 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20210411_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='neighborhood',
            new_name='neighborhood_name',
        ),
        migrations.AddField(
            model_name='emergency_service',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Neighborhood'),
        ),
        migrations.AddField(
            model_name='heath_center',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Neighborhood'),
        ),
        migrations.AddField(
            model_name='police_station',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Neighborhood'),
        ),
    ]
