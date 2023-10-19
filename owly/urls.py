from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('seleccionar_constructora/', views.seleccionar_constructora, name='seleccionar_constructora'),
    path('proyectos_constructora/', views.mostrar_proyectos_constructora, name='mostrar_proyectos_constructora'),


    path('inmueble/', views.InmuebleListCreateView.as_view(), name='inmueble-list-create'),
    path('inmueble/<int:pk>/', views.InmuebleRetrieveUpdateDestroyView.as_view(), name='inmueble-retrieve-update-destroy'),

    path('topología/', views.TopologíaListCreateView.as_view(), name='topología-list-create'),
    path('topología/<int:pk>/', views.TopologíaRetrieveUpdateDestroyView.as_view(), name='topología-retrieve-update-destroy'),

    path('etiqueta/', views.EtiquetaListCreateView.as_view(), name='etiqueta-list-create'),
    path('etiqueta/<int:pk>/', views.EtiquetaRetrieveUpdateDestroyView.as_view(), name='etiqueta-retrieve-update-destroy'),

    path('torre/', views.TorreListCreateView.as_view(), name='torre-list-create'),
    path('torre/<int:pk>/', views.TorreRetrieveUpdateDestroyView.as_view(), name='torre-retrieve-update-destroy'),

    path('usuario/', views.UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuario/<int:pk>/', views.UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-retrieve-update-destroy'),

    path('dirección/', views.DirecciónListCreateView.as_view(), name='dirección-list-create'),
    path('dirección/<int:pk>/', views.DirecciónRetrieveUpdateDestroyView.as_view(), name='dirección-retrieve-update-destroy'),

    path('características/', views.CaracterísticasListCreateView.as_view(), name='características-list-create'),
    path('características/<int:pk>/', views.CaracterísticasRetrieveUpdateDestroyView.as_view(), name='características-retrieve-update-destroy'),

    path('imagen/', views.ImagenListCreateView.as_view(), name='imagen-list-create'),
    path('imagen/<int:pk>/', views.ImagenRetrieveUpdateDestroyView.as_view(), name='imagen-retrieve-update-destroy'),

    path('actualización/', views.ActualizaciónListCreateView.as_view(), name='actualización-list-create'),
    path('actualización/<int:pk>/', views.ActualizaciónRetrieveUpdateDestroyView.as_view(), name='actualización-retrieve-update-destroy'),

    path('solicitud/', views.SolicitudListCreateView.as_view(), name='solicitud-list-create'),
    path('solicitud/<int:pk>/', views.SolicitudRetrieveUpdateDestroyView.as_view(), name='solicitud-retrieve-update-destroy'),

    path('historial/', views.HistorialListCreateView.as_view(), name='historial-list-create'),
    path('historial/<int:pk>/', views.HistorialRetrieveUpdateDestroyView.as_view(), name='historial-retrieve-update-destroy'),

    path('agente/', views.AgenteListCreateView.as_view(), name='agente-list-create'),
    path('agente/<int:pk>/', views.AgenteRetrieveUpdateDestroyView.as_view(), name='agente-retrieve-update-destroy'),

    path('reseñas/', views.ReseñasListCreateView.as_view(), name='reseñas-list-create'),
    path('reseñas/<int:pk>/', views.ReseñasRetrieveUpdateDestroyView.as_view(), name='reseñas-retrieve-update-destroy'),

    path('promociones/', views.PromocionesListCreateView.as_view(), name='promociones-list-create'),
    path('promociones/<int:pk>/', views.PromocionesRetrieveUpdateDestroyView.as_view(), name='promociones-retrieve-update-destroy'),

    path('reservaciones/', views.ReservacionesListCreateView.as_view(), name='reservaciones-list-create'),
    path('reservaciones/<int:pk>/', views.ReservacionesRetrieveUpdateDestroyView.as_view(), name='reservaciones-retrieve-update-destroy'),

    path('contratos/', views.ContratosListCreateView.as_view(), name='contratos-list-create'),
    path('contratos/<int:pk>/', views.ContratosRetrieveUpdateDestroyView.as_view(), name='contratos-retrieve-update-destroy'),

    path('pagos/', views.PagosListCreateView.as_view(), name='pagos-list-create'),
    path('pagos/<int:pk>/', views.PagosRetrieveUpdateDestroyView.as_view(), name='pagos-retrieve-update-destroy'),

    path('eventos/', views.EventosListCreateView.as_view(), name='eventos-list-create'),
    path('eventos/<int:pk>/', views.EventosRetrieveUpdateDestroyView.as_view(), name='eventos-retrieve-update-destroy'),

    path('favoritos/', views.FavoritosListCreateView.as_view(), name='favoritos-list-create'),
    path('favoritos/<int:pk>/', views.FavoritosRetrieveUpdateDestroyView.as_view(), name='favoritos-retrieve-update-destroy'),

    path('documentos/', views.DocumentosListCreateView.as_view(), name='documentos-list-create'),
    path('documentos/<int:pk>/', views.DocumentosRetrieveUpdateDestroyView.as_view(), name='documentos-retrieve-update-destroy'),

    path('apikey/', views.APIKeyListCreateView.as_view(), name='apikey-list-create'),
    path('apikey/<int:pk>/', views.APIKeyRetrieveUpdateDestroyView.as_view(), name='apikey-retrieve-update-destroy'),
    

path('constructora/', views.ConstructoraListCreateView.as_view(), name='constructora-list-create'),
path('constructora/<int:pk>/', views.ConstructoraRetrieveUpdateDestroyView.as_view(), name='constructora-retrieve-update-destroy'),

path('avancedeobra/', views.AvanceDeObraListCreateView.as_view(), name='avancedeobra-list-create'),
path('avancedeobra/<int:pk>/', views.AvanceDeObraRetrieveUpdateDestroyView.as_view(), name='avancedeobra-retrieve-update-destroy'),

path('proyecto/', views.ProyectoListCreateView.as_view(), name='proyecto-list-create'),
path('proyecto/<int:pk>/', views.ProyectoRetrieveUpdateDestroyView.as_view(), name='proyecto-retrieve-update-destroy'),

path('Empresa/', views.EmpresaListCreateView.as_view(), name='Empresa-list-create'),
path('Empresa/<int:pk>/', views.EmpresaRetrieveUpdateDestroyView.as_view(), name='Empresa-retrieve-update-destroy'),

path('etapa/', views.EtapaListCreateView.as_view(), name='etapa-list-create'),
path('etapa/<int:pk>/', views.EtapaRetrieveUpdateDestroyView.as_view(), name='etapa-retrieve-update-destroy'),
path('admin/', admin.site.urls),
path('crear_torre/', views.crear_torre, name='crear_torre'),
path('proyecto_homepage/<int:pk>/', views.proyecto_homepage, name='proyecto_homepage'),
path('inmueble_details/<int:inmueble_id>/', views.inmueble_detail, name='inmueble_details'),
path('mostrar_proyecto/', views.mostrar_proyecto, name='mostrar_proyecto'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
