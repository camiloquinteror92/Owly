# Generated by Django 4.2.6 on 2023-10-13 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_bloque', models.CharField(max_length=100)),
                ('numero_de_unidades', models.PositiveIntegerField()),
                ('descripcion', models.TextField()),
                ('slogan', models.CharField(max_length=200)),
                ('fachada', models.ImageField(upload_to='bloque_fachadas/')),
                ('valor_m2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_m2_terrazza', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_m2_mezzanine', models.DecimalField(decimal_places=2, max_digits=10)),
                ('incremento_por_piso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modalidad_de_venta', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('cedula_o_pasaporte', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Constructora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_etapas', models.PositiveIntegerField()),
                ('fachada', models.ImageField(upload_to='proyecto_fachadas/')),
                ('nombre_corto', models.CharField(max_length=100)),
                ('descripcion_larga', models.TextField()),
                ('estrato', models.PositiveIntegerField()),
                ('categoria', models.CharField(max_length=100)),
                ('notificaciones', models.BooleanField()),
                ('constructora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.constructora')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(max_length=100)),
                ('piso', models.PositiveIntegerField()),
                ('habitaciones', models.PositiveIntegerField()),
                ('baños', models.PositiveIntegerField()),
                ('balcon', models.PositiveIntegerField()),
                ('numero_de_unidad', models.PositiveIntegerField()),
                ('area_construida_u', models.PositiveIntegerField()),
                ('area_balcon_u', models.PositiveIntegerField()),
                ('area_privada_u', models.PositiveIntegerField()),
                ('area_terraza_u', models.PositiveIntegerField()),
                ('area_mezzanine_u', models.PositiveIntegerField()),
                ('bloque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.bloque')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='usuarios/')),
            ],
        ),
        migrations.CreateModel(
            name='ZonaComun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('slogan', models.CharField(max_length=200)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadLead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.lead')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.cliente')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.unidad')),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.usuario'),
        ),
        migrations.CreateModel(
            name='Etapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_etapa', models.PositiveIntegerField()),
                ('tipo_de_bloque', models.CharField(max_length=100)),
                ('numero_de_bloques', models.PositiveIntegerField()),
                ('descripcion', models.TextField()),
                ('avance', models.PositiveIntegerField()),
                ('entrega_estimada', models.DateField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaVinculada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='empresa_logos/')),
                ('nombre', models.CharField(max_length=200)),
                ('rol', models.CharField(max_length=100)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='bloque',
            name='etapa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owly.etapa'),
        ),
    ]
