# Generated by Django 3.2.4 on 2022-09-12 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestorUsuarios', '0008_auto_20220911_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]
