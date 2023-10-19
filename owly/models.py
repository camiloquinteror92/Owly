from django.db import models

def imagen_upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'constructoras/{instance.constructora.nombre}/imagenes/{filename}'

def empresa_logo_upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'constructoras/{instance.constructora.nombre}/empresa_logos/{filename}'

def proyecto_imagen_upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'constructoras/{instance.constructora.nombre}/proyectos/imagenes/{filename}'

def proyecto_logo_upload_path(instance, filename):
    extension = filename.split('.')[-1]
    return f'constructoras/{instance.constructora.nombre}/proyectos/logos/{filename}'

def constructora_logo_upload_path(instance, filename):
    # Obtenemos la extensión del archivo
    extension = filename.split('.')[-1]
    # Generamos la ruta usando el nombre de la constructora y la extensión del archivo
    return f'constructoras/{instance.nombre}/logo.{extension}'


class Constructora(models.Model):
    nombre = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=constructora_logo_upload_path)

    def __str__(self):
        return self.nombre

class AvanceDeObra(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Avance')
    demolicion = models.PositiveIntegerField(default=0, verbose_name='Demolicion')
    excavacion = models.PositiveIntegerField(default=0, verbose_name='Excavacion')
    estructura = models.PositiveIntegerField(default=0, verbose_name='Estructura')
    fachada = models.PositiveIntegerField(default=0, verbose_name='Fachada')
    hidraulica = models.PositiveIntegerField(default=0, verbose_name='Hidraulica')
    electrica = models.PositiveIntegerField(default=0, verbose_name='Electrica')
    extraccion = models.PositiveIntegerField(default=0, verbose_name='Extraccion')
    mamposteria_liviana = models.PositiveIntegerField(default=0, verbose_name='Mamposteria Liviana')
    avance_total = models.PositiveIntegerField(default=0, verbose_name='Avance total')

    def __str__(self):
       return f"{self.nombre} - Demolicion: {self.demolicion}% | Excavacion: {self.excavacion}% | Estructura: {self.estructura}% | Fachada: {self.fachada}% | Hidraulica: {self.hidraulica}% | Electrica: {self.electrica}% | Extraccion: {self.extraccion}% | Mamposteria Liviana: {self.mamposteria_liviana}% | Avance Total: {self.avance_total}%"


class Direccion(models.Model):
    ciudad = models.CharField(max_length=255)
    region_estado = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    coordenadas = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.calle},{self.ciudad}, {self.region_estado}, {self.pais}'



class Etiqueta(models.Model):
    nombre = models.CharField(max_length=255)
    puntos = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Caracteristica(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=empresa_logo_upload_path)
    rol = models.CharField(max_length=100)
    constructora = models.ForeignKey(Constructora, on_delete=models.CASCADE)

    class Meta:
        app_label = 'owly'


class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to=proyecto_imagen_upload_path)
    logo = models.ImageField(upload_to=proyecto_logo_upload_path)
    numero_etapas = models.PositiveIntegerField()
    caracteristicas = models.ManyToManyField(Caracteristica)
    constructora = models.ForeignKey(Constructora, on_delete=models.CASCADE)
    avance_obra = models.ForeignKey(AvanceDeObra, on_delete=models.SET_NULL, null=True, blank=True)
    Empresa = models.ManyToManyField(Empresa)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Etapa(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    numero_de_etapa = models.PositiveIntegerField()
    numero_de_torres = models.PositiveIntegerField()
    fecha_entrega_estimada = models.DateField()
    porcentaje_cuota_inicial = models.PositiveIntegerField()
    avance_obra = models.ManyToManyField(AvanceDeObra)
    caracteristicas = models.ManyToManyField(Caracteristica)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Imagen(models.Model):
    descripcion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to=imagen_upload_path)
    constructora = models.ForeignKey(Constructora, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Tipologia(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE)  # ForeignKey to the Imagen model

    def __str__(self):
        return self.nombre


class Torre(models.Model):
    nombre_descripcion = models.CharField(max_length=255)
    Etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    imagenes = models.ManyToManyField(Imagen)
    def __str__(self):
        return self.nombre_descripcion
    
class Inmueble(models.Model):
    nombre_descripcion = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=24, decimal_places=2)
    habitaciones = models.IntegerField()
    piso = models.IntegerField()
    baños = models.DecimalField(max_digits=3, decimal_places=1)
    terraza = models.BooleanField()
    externo = models.BooleanField ()
    estado = models.CharField(max_length=255)
    caracteristicas = models.ManyToManyField(Caracteristica)
    tipologia = models.ForeignKey(Tipologia, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Etiqueta)
    imagenes = models.ManyToManyField(Imagen)
    torre = models.ForeignKey(Torre, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nombre_descripcion
    

class Actualizacion(models.Model):
    fecha = models.DateField()
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)

class Solicitud(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=255)

class Historial(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Agente(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.EmailField()
    comisiones = models.CharField(max_length=255)
    inmuebles = models.ManyToManyField(Inmueble)

    def __str__(self):
        return self.nombre

class Resena(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha = models.DateField()
    titulo = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    puntuacion = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Promocion(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    descuento = models.CharField(max_length=255)
    inmuebles = models.ManyToManyField(Inmueble)

    def __str__(self):
        return self.descripcion

class Reservacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado = models.CharField(max_length=255)

class Contrato(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    usuario_cliente = models.CharField(max_length=255)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)
    fecha = models.DateField()
    terminos = models.CharField(max_length=255)

class Pago(models.Model):
    cantidad = models.IntegerField()
    fecha = models.DateField()
    metodo = models.CharField(max_length=255)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    estado = models.CharField(max_length=255)

class Evento(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255)
    prioridad_severidad = models.CharField(max_length=255)

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    fecha = models.DateField()

class Documento(models.Model):
    nombre_descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fecha = models.DateField()
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE)

class APIKey(models.Model):
    key = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        app_label = 'owly'


