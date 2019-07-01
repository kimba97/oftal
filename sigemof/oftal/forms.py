from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class PacienteForm(forms.ModelForm):

	class Meta:
		model = Paciente
		fields=['nombrePersona', 'dui', 'direccion', 'telefono', 'fechaNac', 'edad', 
		'sexo', 'correo', 'nombrePadre', 'nombreMadre', 'remitente']

		labels={
		'nombrePersona':'Nombre Paciente',
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
		'dui':forms.TextInput(attrs={'class':'form-control'}),
		'direccion': forms.TextInput(attrs={'class':'form-control'}),
		'telefono':forms.TextInput(attrs={'class':'form-control'}),
		'fechaNac':forms.DateInput(attrs={'class':'form-control'}),
		'edad':forms.TextInput(attrs={'class':'form-control'}),
		'sexo':forms.Select(attrs={'class':'form-control'}),
		'correo':forms.TextInput(attrs={'class':'form-control'}),
		'nombrePadre':forms.TextInput(attrs={'class':'form-control'}),
		'NombreMadre':forms.TextInput(attrs={'class':'form-control'}),
		'remitente':forms.TextInput(attrs={'class':'form-control'})
		}