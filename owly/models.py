from django.db import models

# Constructora
class Constructora(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        app_label = 'owly'

    def __str__(self):
        return self.nombre


# Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='usuarios/')

    class Meta:
        app_label = 'owly'

class Proyecto(models.Model):
    constructora = models.ForeignKey(Constructora, on_delete=models.CASCADE)
    numero_etapas = models.PositiveIntegerField()
    fachada = models.ImageField(upload_to='proyecto_fachadas/')
    nombre_corto = models.CharField(max_length=100)
    descripcion_larga = models.TextField()
    estrato = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100)
    notificaciones = models.BooleanField()

    class Meta:
        app_label = 'owly'
    
    def __str__(self):
        return self.nombre_corto
    

class Etapa(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    numero_de_etapa = models.PositiveIntegerField()
    tipo_de_bloque = models.CharField(max_length=100)
    numero_de_bloques = models.PositiveIntegerField()
    descripcion = models.TextField()
    avance = models.PositiveIntegerField()
    entrega_estimada = models.DateField()
    
    class Meta:
        app_label = 'owly'

    def __str__(self):
        return str(self.numero_de_etapa)


class EmpresaVinculada(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='empresa_logos/')
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=100)

    class Meta:
        app_label = 'owly'

class ZonaComun(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    slogan = models.CharField(max_length=200)

    class Meta:
        app_label = 'owly'

    def __str__(self):
        return self.nombre

class Bloque(models.Model):
    #nombre = models.CharField(max_length=200)--------Solucionar
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    tipo_de_bloque = models.CharField(max_length=100)
    numero_de_unidades = models.PositiveIntegerField()
    descripcion = models.TextField()
    slogan = models.CharField(max_length=200)
    fachada = models.ImageField(upload_to='bloque_fachadas/')
    valor_m2 = models.DecimalField(max_digits=10, decimal_places=2)
    valor_m2_terrazza = models.DecimalField(max_digits=10, decimal_places=2)
    valor_m2_mezzanine = models.DecimalField(max_digits=10, decimal_places=2)
    incremento_por_piso = models.DecimalField(max_digits=10, decimal_places=2)
    modalidad_de_venta = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'owly'
    
    def __str__(self):
        return self.descripcion       

class Tipo(models.Model):
    nombre = models.CharField(max_length=200)
    #nivel = models.ForeignKey('Nivel', related_name="tipos", on_delete=models.CASCADE)
    #area_total = models.PositiveIntegerField()
    #area_balcon = models.PositiveIntegerField()
    #area_construida = models.PositiveIntegerField()
    #precio = models.DecimalField(max_digits=10, decimal_places=2)
    #habitaciones = models.PositiveIntegerField()

    class Meta:
        app_label = 'owly'

    #def __str__(self):---------------Solucionar
        #return self.nombre-----------Solucionar

#class Nivel(models.Model):
    #tipo = models.ForeignKey(Tipo, related_name="niveles", on_delete=models.CASCADE)
    #estilo = models.ForeignKey('Estilo', related_name="niveles_estilo", on_delete=models.CASCADE)

    #class Meta:
        #app_label = 'owly'

#class Estilo(models.Model):
    #nivel = models.ForeignKey(Nivel, related_name="estilos", on_delete=models.CASCADE)
    #tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
   
    #class Meta:
        #app_label = 'owly'

class Unidad(models.Model):
    estatus = models.CharField(max_length=100)
    bloque = models.ForeignKey(Bloque, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    piso = models.PositiveIntegerField()
    habitaciones = models.PositiveIntegerField()
    baños = models.PositiveIntegerField()
    balcon = models.PositiveIntegerField()
    numero_de_unidad = models.PositiveIntegerField()
    area_construida_u = models.PositiveIntegerField()
    area_balcon_u = models.PositiveIntegerField()
    area_privada_u = models.PositiveIntegerField()
    area_terraza_u = models.PositiveIntegerField()
    area_mezzanine_u = models.PositiveIntegerField()
    

    class Meta:
        app_label = 'owly'

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    cedula_o_pasaporte = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'owly'

class UnidadCliente(models.Model):
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        app_label = 'owly'

class Lead(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    class Meta:
        app_label = 'owly'

class UnidadLead(models.Model):
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
   
    class Meta:
        app_label = 'owly'

class APIKey(models.Model):
    key = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        app_label = 'owly'
