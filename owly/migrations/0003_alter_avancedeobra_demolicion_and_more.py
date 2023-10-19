# Generated by Django 4.2.6 on 2023-10-18 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owly', '0002_rename_demolición_avancedeobra_demolicion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avancedeobra',
            name='demolicion',
            field=models.PositiveIntegerField(default=0, verbose_name='Demolicion'),
        ),
        migrations.AlterField(
            model_name='avancedeobra',
            name='electrica',
            field=models.PositiveIntegerField(default=0, verbose_name='Electrica'),
        ),
        migrations.AlterField(
            model_name='avancedeobra',
            name='excavacion',
            field=models.PositiveIntegerField(default=0, verbose_name='Excavacion'),
        ),
        migrations.AlterField(
            model_name='avancedeobra',
            name='extraccionn',
            field=models.PositiveIntegerField(default=0, verbose_name='Extraccion'),
        ),
        migrations.AlterField(
            model_name='avancedeobra',
            name='hidraulica',
            field=models.PositiveIntegerField(default=0, verbose_name='Hidraulica'),
        ),
        migrations.AlterField(
            model_name='avancedeobra',
            name='mamposteria_liviana',
            field=models.PositiveIntegerField(default=0, verbose_name='Mamposteria Liviana'),
        ),
    ]
