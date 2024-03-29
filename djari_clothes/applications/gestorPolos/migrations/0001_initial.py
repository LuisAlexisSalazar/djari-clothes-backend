# Generated by Django 3.2.4 on 2022-09-06 02:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestorUsuarios', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_marca', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Polo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('color', models.CharField(blank=True, choices=[('Rojo', 'Rojo'), ('Verde', 'Verde'), ('Azul', 'Azul'), ('Amarillo', 'Amarillo'), ('Morado', 'Morado'), ('Naranja', 'Naranja'), ('Blanco', 'Blanco'), ('Negro', 'Negro'), ('Celeste', 'Celeste')], max_length=8)),
                ('path_image', models.ImageField(default='\\polos\\default.jpg', upload_to='polos')),
                ('name_modelo', models.CharField(max_length=15)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('price', models.FloatField()),
                ('emprendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestorUsuarios.emprendedor')),
                ('marca', models.ManyToManyField(to='gestorPolos.Marca')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PoloFavorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestorUsuarios.client')),
                ('polo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestorPolos.polo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetallePolo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.CharField(choices=[('S', 'Pequeño (S)'), ('M', 'Mediano (M)'), ('L', 'Grande (L)'), ('XL', 'Extra Grande (XL)')], max_length=2)),
                ('polo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gestorPolos.polo')),
            ],
        ),
    ]
