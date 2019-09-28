from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
		'dui':forms.TextInput(attrs={'class':'form-control'}),
		'direccion': forms.TextInput(attrs={'class':'form-control'}),
		'telefono':forms.TextInput(attrs={'class':'form-control'}),
		'fechaNac':forms.DateInput(attrs={'class':'form-control'}),
		'edad':forms.TextInput(attrs={'class':'form-control'}),
		'sexo':forms.TextInput(attrs={'class':'form-control'}),
		'correo':forms.TextInput(attrs={'class':'form-control'}),
		'nombrePadre':forms.TextInput(attrs={'class':'form-control'}),
		'nombreMadre':forms.TextInput(attrs={'class':'form-control'}),
		'remitente':forms.TextInput(attrs={'class':'form-control'})
		}


class LenteForm(forms.ModelForm):

	class Meta:
		model = Lente
		fields=['codigo', 'color', 'marca', 'cantidad', 'precioCompra']

		labels={
		'codigo':'Codigo',
		'color':'Color',
		'Marca':'marca',
		'cantidad':'Cantidad',
		'precioCompra':'PrecioCompra'
		}

		widgets={
		'codigo':forms.TextInput(attrs={'class':'form-control'}),
		'color':forms.TextInput(attrs={'class':'form-control'}),
		'marca': forms.TextInput(attrs={'class':'form-control'}),
		'cantidad':forms.TextInput(attrs={'class':'form-control'}),
		'precioCompra':forms.TextInput(attrs={'class':'form-control'})
		}




class CristalForm(forms.ModelForm):

	class Meta:
		model = Cristal
		fields=['codigo', 'graduacion', 'material', 'color', 'marca', 'cantidad', 'precioCompra']

		labels={
		'codigo':'Codigo',
		'graduacion':'Graduacion',
		'material':'Material',
		'color':'Color',
		'Marca':'marca',
		'cantidad':'Cantidad',
		'precioCompra':'PrecioCompra'
		}

		widgets={
		'codigo':forms.TextInput(attrs={'class':'form-control'}),
		'graduacion': forms.TextInput(attrs={'class': 'form-control'}),
		'material': forms.TextInput(attrs={'class': 'form-control'}),
		'color':forms.TextInput(attrs={'class':'form-control'}),
		'marca': forms.TextInput(attrs={'class':'form-control'}),
		'cantidad':forms.TextInput(attrs={'class':'form-control'}),
		'precioCompra':forms.TextInput(attrs={'class':'form-control'})
		}



