# Generated by Django 4.2.6 on 2023-10-18 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owly', '0004_rename_extraccionn_avancedeobra_extraccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='avance_obra',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='avance_obra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='owly.avancedeobra'),
        ),
    ]