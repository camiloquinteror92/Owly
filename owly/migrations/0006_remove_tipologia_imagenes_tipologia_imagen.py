# Generated by Django 4.2.6 on 2023-10-19 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owly', '0005_remove_proyecto_avance_obra_proyecto_avance_obra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipologia',
            name='imagenes',
        ),
        migrations.AddField(
            model_name='tipologia',
            name='imagen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='owly.imagen'),
            preserve_default=False,
        ),
    ]
