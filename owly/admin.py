from django.contrib import admin
from .models import Constructora, Proyecto, Usuario, EmpresaVinculada, ZonaComun, Etapa, Bloque, Unidad, Tipo

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_corto']
    search_fields = ['nombre_corto']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido']
    search_fields = ['nombre', 'apellido']

@admin.register(EmpresaVinculada)
class EmpresaVinculadaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'rol']
    search_fields = ['nombre']

@admin.register(ZonaComun)
class ZonaComunAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'slogan']
    search_fields = ['descripcion']

@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero_de_etapa', 'tipo_de_bloque']
    search_fields = ['tipo_de_bloque']

@admin.register(Bloque)
class BloqueAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'slogan']
    search_fields = ['descripcion']

#@admin.register(Nivel)
#class NivelAdmin(admin.ModelAdmin):
#    list_display = ['id']

#@admin.register(Estilo)
#class EstiloAdmin(admin.ModelAdmin):
#    list_display = ['id']

@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ['id', 'estatus', 'piso']
    search_fields = ['estatus']

@admin.register(Constructora)
class ConstructoraAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

from django.contrib import admin
from .models import Tipo

from django.contrib import admin
from .models import Tipo

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_filter = []  # Asegúrate de que los campos aquí sean válidos para tu modelo Tipo

# Registrar otros modelos en el admin si es necesario.

