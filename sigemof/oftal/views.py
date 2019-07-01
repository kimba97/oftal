from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  *
from django.urls import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import permission_required

from oftal.forms import *


# Create your views here.

class CreatePaciente(CreateView):
	model=Paciente
	form_class=PacienteForm
	template_name='RegistrarPaciente.html'
	success_url='/ListaPaciente/'

class ListPaciente(ListView):
	model = Paciente
	template_name='verPaciente.html'

class UpdatePaciente(UpdateView):
	model=Paciente
	form_class=PacienteForm
	template_name='RegistrarPaciente.html'
	success_url='/ListaPaciente/'

def UpdatePaciente(request, id):
	paciente=Paciente.objects.get(id=id)
	if request.method == 'GET':
		form = PacienteForm(instance=paciente)
	else:
		form = PacienteForm(request.POST, instance=paciente)
		if form.is_valid():
			form.save()
		return redirect('ListaPaciente')
	return render(request, 'RegistrarPaciente.html', {'form':form})


def DeletePaciente(request,id):
	paciente=Paciente.objects.get(id=id)
	if request.method == 'POST':
		paciente.delete()
		return redirect('ListaPaciente')
	return render(request, 'EliminarPaciente.html', {'Paciente': paciente})	
