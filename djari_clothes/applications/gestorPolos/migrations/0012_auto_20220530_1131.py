# Generated by Django 3.2 on 2022-05-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorPolos', '0011_auto_20220528_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='polo',
            name='path_image',
            field=models.ImageField(default='\\polos\\default.jpg', upload_to='polos'),
        ),
        migrations.AlterField(
            model_name='polofavorites',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
