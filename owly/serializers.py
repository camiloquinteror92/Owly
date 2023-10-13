
from rest_framework import serializers
from .models import Proyecto, Usuario, EmpresaVinculada, ZonaComun
from .models import Etapa, Bloque, Unidad

class EmpresaVinculadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaVinculada
        fields = '__all__'

class ZonaComunSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonaComun
        fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
    empresas_vinculadas = EmpresaVinculadaSerializer(many=True, required=False)
    zonas_comunes = ZonaComunSerializer(many=True, required=False)

    class Meta:
        model = Proyecto
        fields = '__all__'

    def create(self, validated_data):
        empresas_data = validated_data.pop('empresas_vinculadas', [])
        zonas_data = validated_data.pop('zonas_comunes', [])
        proyecto = Proyecto.objects.create(**validated_data)

        for empresa_data in empresas_data:
            EmpresaVinculada.objects.create(proyecto=proyecto, **empresa_data)

        for zona_data in zonas_data:
            ZonaComun.objects.create(proyecto=proyecto, **zona_data)

        return proyecto

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'



class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields = '__all__'

class BloqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloque
        fields = '__all__'

#class NivelSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Nivel
        #fields = '__all__'

#class EstiloSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Estilo
        #fields = '__all__'

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'
