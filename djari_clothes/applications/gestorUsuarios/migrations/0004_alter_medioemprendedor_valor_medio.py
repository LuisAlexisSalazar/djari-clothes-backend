# Generated by Django 3.2.4 on 2022-09-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorUsuarios', '0003_alter_medioemprendedor_link_medio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medioemprendedor',
            name='valor_medio',
            field=models.CharField(max_length=25),
        ),
    ]
