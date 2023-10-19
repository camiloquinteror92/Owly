from django.contrib import admin
from .models import *
from .models import Torre
from .forms import TorreForm


@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Inmueble._meta.fields]

@admin.register(Tipologia)
class TopologíaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tipologia._meta.fields]

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Etiqueta._meta.fields]


class TorreAdmin(admin.ModelAdmin):
    form = TorreForm
    list_display = ('nombre_descripcion', 'Etapa')
    search_fields = ('nombre_descripcion', 'Etapa__nombre')
    list_filter = ('Etapa__proyecto__nombre',)

# Registra el modelo Torre y la clase personalizada del administrador
admin.site.register(Torre, TorreAdmin)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Usuario._meta.fields]

@admin.register(Direccion)
class DirecciónAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Direccion._meta.fields]

@admin.register(Caracteristica)
class CaracterísticasAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Caracteristica._meta.fields]

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Imagen._meta.fields]

@admin.register(Actualizacion)
class ActualizaciónAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Actualizacion._meta.fields]

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Solicitud._meta.fields]

@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Historial._meta.fields]

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Agente._meta.fields]

@admin.register(Resena)
class ReseñasAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Resena._meta.fields]

@admin.register(Promocion)
class PromocionesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Promocion._meta.fields]

@admin.register(Reservacion)
class ReservacionesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reservacion._meta.fields]

@admin.register(Contrato)
class ContratosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contrato._meta.fields]

@admin.register(Pago)
class PagosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pago._meta.fields]

@admin.register(Evento)
class EventosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Evento._meta.fields]

@admin.register(Favorito)
class FavoritosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Favorito._meta.fields]

@admin.register(Documento)
class DocumentosAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Documento._meta.fields]

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in APIKey._meta.fields]

@admin.register(Constructora)
class ConstructoraAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Constructora._meta.fields]

@admin.register(AvanceDeObra)
class AvanceDeObraAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AvanceDeObra._meta.fields]

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Proyecto._meta.fields]

@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Etapa._meta.fields]

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Empresa._meta.fields]

