# Generated by Django 3.2 on 2022-05-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorVentas', '0004_auto_20220528_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsale',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
