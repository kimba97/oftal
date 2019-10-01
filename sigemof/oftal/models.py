from __future__ import unicode_literals

from django.db import models
from oftal.choices import SEX_CHOICES

# Create your models here.

class Persona(models.Model):
	nombrePersona=models.CharField(max_length=200)
	apellidoPersona=models.CharField(max_length=200)
	dui=models.CharField(max_length=10, unique=True)
	direccion=models.CharField(max_length=250)
	telefono=models.CharField(max_length=9)
	fechaNac=models.DateTimeField()
	edad=models.IntegerField()
	sexo=models.CharField(max_length=20)

	class Meta:
		verbose_name='Persona'
		verbose_name_plural='Personas'
	def __str__(self):
		return '%s' %(self.nombrePersona)

class Lente(models.Model):
	codigo=models.CharField(max_length=20)
	color=models.CharField(max_length=30)
	marca=models.CharField(max_length=50)
	tamano=models.FloatField(max_length=50)
#	cantidad=models.IntegerField()
#	precioCompra=models.FloatField()

	class Meta:
		verbose_name='Lente'
		verbose_name_plural='Lentes'
	def __str__(self):
		return '%s' %(self.codigo)

class FacturaLente(models.Model):
	descripcion= models.CharField(max_length=50)
	precio = models.FloatField(null=True)
	total = models.FloatField(null=True)
	cantidad = models.IntegerField(null=True)
	
#	class Meta:
#		verbose_name='FacturaVenta'
#		verbose_name_pural='FacturaVentas'
	def __str__(self):
		return '%s' %(self.id)

class Cristal(models.Model):
	codigo = models.CharField(max_length=20)
	esfera = models.CharField(max_length=20)
	cilindro = models.CharField(max_length=20)
	eje = models.CharField(max_length=20)
	prisma = models.CharField(max_length=20)
	base = models.CharField(max_length=20)
	adicion = models.CharField(max_length=20)
	graduacion = models.CharField(max_length=20)
#	material=models.CharField(max_length=30)
	color = models.CharField(max_length=30)

	codigod = models.CharField(max_length=20)
	esferad = models.CharField(max_length=20)
	cilindrod = models.CharField(max_length=20)
	ejed = models.CharField(max_length=20)
	prismad = models.CharField(max_length=20)
	based = models.CharField(max_length=20)
	adiciond = models.CharField(max_length=20)
	graduaciond = models.CharField(max_length=20)
	colord = models.CharField(max_length=30)
	factura = models.ForeignKey(FacturaLente, on_delete=models.CASCADE,null=True, blank=True)

	class Meta:
		verbose_name='Cristal'
		verbose_name_plural='Cristals'
	def __str__(self):
		return '%s' %(self.codigo)

class Secretaria(Persona):
	isss=models.CharField(max_length=12, unique=True)
	afp=models.CharField(max_length=9, unique=True)
	class Meta:
		verbose_name='Secretaria'
		verbose_name_plural='Secretarias'
	def __str__(self):
		return '%s' %(self.nombrePersona)

class Doctora(Secretaria):
	jvpm=models.CharField(max_length=10, unique=True)
	class Meta:
		verbose_name='Doctora'
		verbose_name_plural='Doctoras'
	def __str__(self):
		return '%s' %(self.nombrePersona)

class Paciente(Persona):
	
	correo=models.EmailField(null=True, blank=True)
	nombrePadre=models.CharField(max_length=20,null=True, blank=True)
	nombreMadre=models.CharField(max_length=200,null=True, blank=True)
	remitente=models.CharField(max_length=50)
	class Meta:
		verbose_name='Paciente'
		verbose_name_plural='Pacientes'
	def __str__(self):
		return '%s' %(self.nombrePersona)

class FacturaVenta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True)
    codigoFactura = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    lente = models.ForeignKey(Cristal, on_delete=models.CASCADE, blank=True)
    aro = models.ForeignKey(Lente, on_delete=models.CASCADE, blank=True)
    precioVenta = models.FloatField()
    cantidad = models.IntegerField()
    total = models.FloatField()

    class Meta:
        verbose_name='FacturaVenta'
        verbose_name_plural='FacturaVentas'
    def __str__(self):
        return '%s' %(self.id)

class Expediente(models.Model):
	NumExp=models.CharField(max_length=50, unique=True)
	paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
	class Meta:
		verbose_name='Expediente'
		verbose_name_plural='Expedientes'
	def __str__(self):
		return '%s' %(self.paciente.nombrePersona)

class Consulta(models.Model):
	fecha=models.DateField()
	diag=models.CharField(max_length=500)
	expedientePac=models.ForeignKey(Expediente, on_delete=models.CASCADE, null=True, blank=True)
	class Meta:
		verbose_name='Consulta'
		verbose_name_plural='Consultas'
	def __str__(self):
		return '%s' %(self.id)

class Cita(models.Model):
	fecha=models.DateField()
	horaI=models.CharField(max_length=10)
	horaF=models.CharField(max_length=10)
	estado=models.CharField(max_length=20)
	paciCita=models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
	class Meta:
		verbose_name='Cita'
		verbose_name_plural='Citas'
	def __str__(self):
		return '%s' %(self.id)







#class FacturaVenta(models.Model):
#	paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE,null=True, blank=True)
#	codigoFactura = models.IntegerField(null=True)
#	descripcion = models.CharField(max_length=100,null=True)
#	lente = models.ForeignKey(Cristal, on_delete=models.CASCADE,null=True, blank=True)
#	aro = models.ForeignKey(Lente, on_delete=models.CASCADE,null=True, blank=True)
#	precioVenta = models.FloatField(null=True)
#	cantidad = models.IntegerField(null=True)
#	total = models.FloatField(null=True)

#	class Meta:
#		verbose_name='FacturaVenta'
#		verbose_name_pural='FacturaVentas'
#	def __str__(self):
#		return '%s' %(self.id)











