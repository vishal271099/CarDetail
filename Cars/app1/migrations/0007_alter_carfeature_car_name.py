# Generated by Django 3.2.12 on 2023-03-27 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20230327_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carfeature',
            name='car_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.car'),
        ),
    ]
