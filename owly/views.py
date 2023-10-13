from rest_framework import generics
from .models import Proyecto, Usuario, Etapa, Bloque, Unidad
from .serializers import ProyectoSerializer, UsuarioSerializer, EtapaSerializer, BloqueSerializer, UnidadSerializer

# Proyecto Views
class ProyectoListCreateView(generics.ListCreateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class ProyectoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

    # Overriding the update method to handle nested serializers and create related objects
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        empresas_data = serializer.validated_data.pop('empresas_vinculadas', [])
        zonas_data = serializer.validated_data.pop('zonas_comunes', [])
        
        # Updating the main Proyecto object
        proyecto = serializer.save()
        
        # Handling related EmpresaVinculada objects
        for empresa_data in empresas_data:
            EmpresaVinculada.objects.update_or_create(proyecto=proyecto, defaults=empresa_data)

        # Handling related ZonaComun objects
        for zona_data in zonas_data:
            ZonaComun.objects.update_or_create(proyecto=proyecto, defaults=zona_data)

# Usuario Views
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Etapa Views
class EtapaListCreateView(generics.ListCreateAPIView):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer

class EtapaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer

# Bloque Views
class BloqueListCreateView(generics.ListCreateAPIView):
    queryset = Bloque.objects.all()
    serializer_class = BloqueSerializer

class BloqueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bloque.objects.all()
    serializer_class = BloqueSerializer

# Nivel Views
#class NivelListCreateView(generics.ListCreateAPIView):
#    queryset = Nivel.objects.all()
#    serializer_class = NivelSerializer

#class NivelDetailView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Nivel.objects.all()
#    serializer_class = NivelSerializer

# Estilo Views
#class EstiloListCreateView(generics.ListCreateAPIView):
#    queryset = Estilo.objects.all()
#    serializer_class = EstiloSerializer

#class EstiloDetailView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Estilo.objects.all()
#    serializer_class = EstiloSerializer

# Unidad Views
class UnidadListCreateView(generics.ListCreateAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer

class UnidadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
