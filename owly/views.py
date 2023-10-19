from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import Constructora, Proyecto, Inmueble, Torre, Etapa, Caracteristica, Etiqueta, Imagen, Tipologia
from .forms import TorreForm

class InmuebleListCreateView(generics.ListCreateAPIView):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer

class InmuebleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer

class TopologíaListCreateView(generics.ListCreateAPIView):
    queryset = Tipologia.objects.all()
    serializer_class = TopologiaSerializer

class TopologíaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tipologia.objects.all()
    serializer_class = TopologiaSerializer

class EtiquetaListCreateView(generics.ListCreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class EtiquetaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class TorreListCreateView(generics.ListCreateAPIView):
    queryset = Torre.objects.all()
    serializer_class = TorreSerializer

class TorreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Torre.objects.all()
    serializer_class = TorreSerializer

class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class DirecciónListCreateView(generics.ListCreateAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class DirecciónRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class CaracterísticasListCreateView(generics.ListCreateAPIView):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer

class CaracterísticasRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer

class ImagenListCreateView(generics.ListCreateAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

class ImagenRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

class ActualizaciónListCreateView(generics.ListCreateAPIView):
    queryset = Actualizacion.objects.all()
    serializer_class = ActualizaciónSerializer

class ActualizaciónRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actualizacion.objects.all()
    serializer_class = ActualizaciónSerializer

class SolicitudListCreateView(generics.ListCreateAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

class SolicitudRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

class HistorialListCreateView(generics.ListCreateAPIView):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer

class HistorialRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Historial.objects.all()
    serializer_class = HistorialSerializer

class AgenteListCreateView(generics.ListCreateAPIView):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer

class AgenteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer

class ReseñasListCreateView(generics.ListCreateAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

class ReseñasRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

class PromocionesListCreateView(generics.ListCreateAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionesSerializer

class PromocionesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionesSerializer

class ReservacionesListCreateView(generics.ListCreateAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer

class ReservacionesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer

class ContratosListCreateView(generics.ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class ContratosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class PagosListCreateView(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class PagosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class EventosListCreateView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class FavoritosListCreateView(generics.ListCreateAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class FavoritosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class DocumentosListCreateView(generics.ListCreateAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class DocumentosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class APIKeyListCreateView(generics.ListCreateAPIView):
    queryset = APIKey.objects.all()
    serializer_class = APIKeySerializer

class APIKeyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = APIKey.objects.all()
    serializer_class = APIKeySerializer


class ConstructoraListCreateView(generics.ListCreateAPIView):
    queryset = Constructora.objects.all()
    serializer_class = ConstructoraSerializer

class ConstructoraRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Constructora.objects.all()
    serializer_class = ConstructoraSerializer

class AvanceDeObraListCreateView(generics.ListCreateAPIView):
    queryset = AvanceDeObra.objects.all()
    serializer_class = AvanceDeObraSerializer

class AvanceDeObraRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AvanceDeObra.objects.all()
    serializer_class = AvanceDeObraSerializer

class ProyectoListCreateView(generics.ListCreateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class ProyectoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class EtapaListCreateView(generics.ListCreateAPIView):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer

class EtapaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer

class EmpresaListCreateView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer

def mostrar_proyectos_constructora(request):
    constructora_id = request.GET.get('constructora_id')
    proyectos = Proyecto.objects.filter(constructora_id=constructora_id)
    return render(request, 'mostrar_proyecto.html', {'proyectos': proyectos})

# views.py (añadir a lo que ya tienes)
def mostrar_proyecto(request):
    constructora_id = request.GET.get('constructora_id')
    proyectos = Proyecto.objects.filter(constructora_id=constructora_id)
    return render(request, 'mostrar_proyecto.html', {'proyectos': proyectos})

def seleccionar_constructora(request):
    constructoras = Constructora.objects.all()
    return render(request, 'seleccionar_constructora.html', {'constructoras': constructoras})

def crear_torre(request):
    if request.method == 'POST':
        form = TorreForm(request.POST, request.FILES)
        if form.is_valid():
            torre = form.save()
            return redirect('detalle_torre', torre_id=torre.id)  # Redirige a la página de detalles de la torre recién creada
    else:
        form = TorreForm()
    
    return render(request, 'crear_torre.html', {'form': form})

# views.py - Vista proyecto_homepage
def proyecto_homepage(request, pk):
    # Recuperar el proyecto específico basado en el ID proporcionado (pk)
    proyecto = get_object_or_404(Proyecto, id=pk)
    
    # Obtener la etapa asociada con el proyecto
    etapa = proyecto.etapa_set.first()  # Aquí asumo que un proyecto tiene una única etapa, ajusta según tu modelo
    
    # Obtener las torres asociadas con la etapa
    torres = Torre.objects.filter(Etapa=etapa)
    
    # Obtener los inmuebles asociados con las torres
    inmuebles = Inmueble.objects.filter(torre__in=torres)
    
    # TODO: Determinar el precio más barato del apartamento. Esta lógica dependerá de tus modelos y datos.
    cheapest_apartment_price = None  # Valor de marcador de posición
    
    # Obtener los datos de avance de obra asociados con el proyecto
    avance_de_obra = {
        'demolicion': proyecto.avance_obra.demolicion,
        'excavacion': proyecto.avance_obra.excavacion,
        'estructura': proyecto.avance_obra.estructura,
        # ... (agrega los otros campos de avance de obra)
    }
    
    # Pasar los datos del proyecto, inmuebles, precio más barato y avance de obra a la plantilla
    context = {
        'proyecto': proyecto,
        'inmuebles': inmuebles,
        'cheapest_apartment_price': cheapest_apartment_price,
        'avance_de_obra': avance_de_obra
    }
    return render(request, 'project_homepage.html', context)


def inmueble_detail(request, inmueble_id):
    # Obtener el inmueble específico según su ID
    inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
    
    # Obtener las características asociadas al inmueble
    caracteristicas = inmueble.caracteristicas.all()
    
    # Obtener las etiquetas asociadas al inmueble
    etiquetas = inmueble.etiquetas.all()
    
    # Obtener las imágenes asociadas al inmueble
    imagenes = inmueble.imagenes.all()
    
    # Obtener la tipología del inmueble
    tipologia = inmueble.tipologia
    
    # Obtener la torre (si está asociada) del inmueble
    torre = inmueble.torre

    # Aquí puedes agregar cualquier otra información relacionada con el inmueble que desees mostrar en la vista.

    # Luego, renderizar la plantilla de detalle de inmueble y pasar todos los datos como contexto
    return render(request, 'inmueble_detail.html', {
        'inmueble': inmueble,
        'caracteristicas': caracteristicas,
        'etiquetas': etiquetas,
        'imagenes': imagenes,
        'tipologia': tipologia,
        'torre': torre,
    })