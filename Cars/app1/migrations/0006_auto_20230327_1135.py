# Generated by Django 3.2.12 on 2023-03-27 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20230327_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardimension',
            name='car_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimension_of_car', to='app1.car'),
        ),
        migrations.AlterField(
            model_name='carfeature',
            name='car_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_of_car', to='app1.car'),
        ),
        migrations.AlterField(
            model_name='carperfomance',
            name='car_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performance_of_car', to='app1.car'),
        ),
        migrations.AlterField(
            model_name='carsafety',
            name='car_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='safety_of_car', to='app1.car'),
        ),
    ]
