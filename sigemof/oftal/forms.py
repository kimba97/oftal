from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .choices import *

class PacienteForm(forms.ModelForm):

	class Meta:
		model = Paciente
		fields=['nombrePersona', 'apellidoPersona', 'dui', 'direccion', 'telefono', 'fechaNac', 'edad',
		'sexo', 'correo', 'nombrePadre', 'nombreMadre', 'remitente']

		labels={
		'nombrePersona':'Nombre Paciente',
		'apellidoPersona': 'Apellido',
		'dui':'DUI',
		'direccion':'Dirección',
		'telefono':'Telefono',
		'fechaNac':'Fecha de Nacimiento',
		'edad':'Edad',
		'sexo':'Sexo',
		'correo':'Correo',
		'nombrePadre':'Nombre del padre',
		'NombreMadre':'Nombre de la madre',
		'remitente':'Nombre del remitente'
		}

		widgets={
		'nombrePersona':forms.TextInput(attrs={'class':'form-control'}),
		'apellidoPersona':forms.TextInput(attrs={'class':'form-control'}),
		'dui':forms.TextInput(attrs={'class':'form-control','readonly':'True', 'disabled': 'True'}),
		'direccion': forms.TextInput(attrs={'class':'form-control'}),
		'telefono':forms.TextInput(attrs={'class':'form-control'}),
		'fechaNac':forms.DateInput(attrs={'class':'form-control'}),
		'edad':forms.TextInput(attrs={'class':'form-control'}),
		'sexo':forms.TextInput(attrs={'class':'form-control','readonly':'True', 'disabled': 'True'}),
		'correo':forms.TextInput(attrs={'class':'form-control'}),
		'nombrePadre':forms.TextInput(attrs={'class':'form-control'}),
		'nombreMadre':forms.TextInput(attrs={'class':'form-control'}),
		'remitente':forms.TextInput(attrs={'class':'form-control'})
		}


class AroForm(forms.ModelForm):

	class Meta:
		model = Aro
		fields=['codigo', 'color', 'marca', 'tamano']

		labels={
		'codigo':'Codigo',
		'color':'Color',
		'Marca':'marca',
		'tamano': 'tamano',
#		'cantidad':'Cantidad',
#		'precioCompra':'PrecioCompra'
		}

		widgets={
		'codigo':forms.TextInput(attrs={'class':'form-control'}),
		'color':forms.TextInput(attrs={'class':'form-control'}),
		'marca': forms.TextInput(attrs={'class':'form-control'}),
		'tamano': forms.TextInput(attrs={'class': 'form-control'}),
#		'cantidad':forms.TextInput(attrs={'class':'form-control'}),
#		'precioCompra':forms.TextInput(attrs={'class':'form-control'})
		}




class LenteForm(forms.ModelForm):

	class Meta:
		model = Lente
		fields=['codigo', 'esfera', 'cilindro', 'eje', 'prisma', 'base', 'adicion', 'graduacion', 'color', 'esferad', 'cilindrod', 'ejed', 'prismad', 'based', 'adiciond', 'graduaciond', 'colord']

		labels={
		'codigo':'Codigo OI',
		'esfera': 'Esfera OI',
		'cilindro': 'Cilindro OI',
		'eje': 'Eje OI',
		'prisma': 'Prisma OI',
		'base': 'Base OI',
		'adicion': 'Adicion OI',
		'graduacion':'Graduacion OI',
#		'material':'Material',
		'color':'Color OI',

		'esferad': 'Esfera OD',
		'cilindrod': 'Cilindro OD',
		'ejed': 'Eje OD',
		'prismad': 'Prisma OD',
		'based': 'Base OD',
		'adiciond': 'Adicion OD',
		'graduaciond': 'Graduacion OD',
#		'material':'Material',
		'colord': 'Color OD',
#		'Marca':'marca',
#		'cantidad':'Cantidad',
#		'precioCompra':'PrecioCompra'
		}

		widgets={

		'codigo':forms.TextInput(attrs={'class':'form-control'}),
		'esfera': forms.TextInput(attrs={'class': 'form-control'}),
		'cilindro': forms.TextInput(attrs={'class': 'form-control'}),
		'eje': forms.TextInput(attrs={'class': 'form-control'}),
		'prisma': forms.TextInput(attrs={'class': 'form-control'}),
		'base': forms.TextInput(attrs={'class': 'form-control'}),
		'adicion': forms.TextInput(attrs={'class': 'form-control'}),
		'graduacion': forms.TextInput(attrs={'class': 'form-control'}),
#		'material': forms.TextInput(attrs={'class': 'form-control'}),
		'color':forms.TextInput(attrs={'class':'form-control'}),

		'esferad': forms.TextInput(attrs={'class': 'form-control'}),
		'cilindrod': forms.TextInput(attrs={'class': 'form-control'}),
		'ejed': forms.TextInput(attrs={'class': 'form-control'}),
		'prismad': forms.TextInput(attrs={'class': 'form-control'}),
		'based': forms.TextInput(attrs={'class': 'form-control'}),
		'adiciond': forms.TextInput(attrs={'class': 'form-control'}),
		'graduaciond': forms.TextInput(attrs={'class': 'form-control'}),
#		'material': forms.TextInput(attrs={'class': 'form-control'}),
		'colord': forms.TextInput(attrs={'class': 'form-control'}),
#		'marca': forms.TextInput(attrs={'class':'form-control'}),
#		'cantidad':forms.TextInput(attrs={'class':'form-control'}),
#		'precioCompra':forms.TextInput(attrs={'class':'form-control'})
		}

class CitaForm(forms.ModelForm):

	class Meta:
		model = Cita
		fields=['fecha', 'horaI', 'horaF', 'estado', 'paciCita']

		labels={
		'fecha':'Fecha',
		'horaI': 'Hora de Inicio',
		'horaF': 'Hora de Fin',
		'estado': 'Estado de Cita',
		'paciCita': 'Nombre del Paciente',
		}

		widgets={
		'fecha':forms.TextInput(attrs={'class': 'form-control','readonly':'True'}),
			'horaI': forms.DateInput(attrs={'class': 'form-control','readonly':'True'}),
			'horaF': forms.DateInput(attrs={'class': 'form-control','readonly':'True'}),
			#STATUS_CHOICES = ((PROGRAMADA, "programada"), (REPROGRAMADA, "reprogramada"), (REALIZADA, "realizada"))
			'estado': forms.Select(attrs={'class': 'form-control'}, choices=ESTADO_CHOICES),
			'paciCita': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}),
			}

class UpdateForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = User
		fields = [
		'username',
		'first_name',
		'last_name',
		'email',
		]
		labels = {
		'username' : 'Nombre de Usuario',
		'first_name': 'Nombre',
		'last_name': 'Apellidos',
		'email': 'Correo',
		}

		def save(self, commit = True):
			user = super().save(commit = False)
			user.isSecretaria=True
			user.save()

			group=Group.objects.get(name='Secretaria')
			user.groups.add(group)

			if commit:
				user.save()
			return user