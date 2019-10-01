from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
	list_display = ('nombrePersona', 'apellidoPersona', 'dui', 'direccion', 'telefono', 'fechaNac', 'edad')
admin.site.register(Persona,PersonaAdmin)

class LenteAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'color', 'marca', 'tamano')
admin.site.register(Lente,LenteAdmin)

class SecretariaAdmin(admin.ModelAdmin):
	list_display = ('nombrePersona', 'dui', 'direccion', 'telefono', 'fechaNac', 'edad', 'isss', 'afp')
admin.site.register(Secretaria,SecretariaAdmin)

class DoctoraAdmin(admin.ModelAdmin):
	list_display = ('nombrePersona', 'dui', 'direccion', 'telefono', 'fechaNac', 'edad', 'isss', 'afp', 'jvpm')
admin.site.register(Doctora,DoctoraAdmin)

class ConsultaAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'diag', 'expedientePac')
admin.site.register(Consulta,ConsultaAdmin)

class ExpedienteAdmin(admin.ModelAdmin):
	list_display = ('NumExp', 'paciente')
admin.site.register(Expediente,ExpedienteAdmin)

class PacienteAdmin(admin.ModelAdmin):
	list_display = ('nombrePersona', 'dui', 'direccion', 'telefono', 'fechaNac', 'edad', 'remitente')
admin.site.register(Paciente,PacienteAdmin)

class CristalAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'esfera', 'cilindro', 'eje', 'prisma', 'base', 'adicion', 'graduacion', 'color', 'codigod', 'esferad', 'cilindrod', 'ejed', 'prismad', 'based', 'adiciond', 'graduaciond', 'colord')
admin.site.register(Cristal,CristalAdmin)

class FacturaVentaAdmin(admin.ModelAdmin):
	list_display = ('paciente', 'codigoFactura', 'descripcion', 'lente', 'aro', 'precioVenta', 'cantidad', 'total')
admin.site.register(FacturaVenta,FacturaVentaAdmin)

class CitaAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'horaI', 'horaF', 'estado', 'paciCita')
admin.site.register(Cita,CitaAdmin)

class FacturaLenteAdmin(admin.ModelAdmin):
	list_display = ('descripcion', 'precio', 'total', 'cantidad')
admin.site.register(FacturaLente,FacturaLenteAdmin)