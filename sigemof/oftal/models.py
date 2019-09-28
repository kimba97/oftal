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
#	marca=models.CharField(max_length=50)
#	cantidad=models.IntegerField()
#	precioCompra=models.FloatField()

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


class FacturaVenta(models.Model):

#	class Meta:
#		verbose_name='FacturaVenta'
#		verbose_name_pural='FacturaVentas'
	def __str__(self):
		return '%s' %(self.id)











