from django.contrib import admin
from django.urls import path
from .views import (
    ProyectoListCreateView, ProyectoDetailView,
    EtapaListCreateView, EtapaDetailView,
    BloqueListCreateView, BloqueDetailView,
    UnidadListCreateView, UnidadDetailView,
    UsuarioListCreateView, UsuarioDetailView
)

urlpatterns = [
    path('proyectos/', ProyectoListCreateView.as_view(), name='proyecto-list-create'),
    path('proyectos/<int:pk>/', ProyectoDetailView.as_view(), name='proyecto-detail'),

    path('proyectos/<int:proyecto_id>/etapas/', EtapaListCreateView.as_view(), name='etapa-list-create'),
    path('etapas/<int:pk>/', EtapaDetailView.as_view(), name='etapa-detail'),

    path('etapas/<int:etapa_id>/bloques/', BloqueListCreateView.as_view(), name='bloque-list-create'),
    path('bloques/<int:pk>/', BloqueDetailView.as_view(), name='bloque-detail'),

    path('bloques/<int:bloque_id>/unidades/', UnidadListCreateView.as_view(), name='unidad-list-create'),
    path('unidades/<int:pk>/', UnidadDetailView.as_view(), name='unidad-detail'),

    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('admin/', admin.site.urls),
]

