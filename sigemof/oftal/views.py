from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  *
from django.urls import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import permission_required
from django.http.response import HttpResponseRedirect
from oftal.forms import *
from django.contrib.auth import authenticate, login


# Create your views here.

def index(request):
    return render(request, 'index.html')

def Base(request):
	return render(request, 'Base.html')

def inicio(request):
	return render(request, 'inicio.html')

class CreatePaciente(CreateView):
	model=Expediente
	form_class=PacienteForm
	template_name='RegistrarPaciente.html'
	success_url='/ListaPaciente/'

def ListPaciente(request):
	pacientes = Paciente.objects.all()
	expedientes = Expediente.objects.all()
	noexp = []
	for p in pacientes:
		if Expediente.objects.filter(paciente_id=p.id).exists() == False:
			noexp.append(p)
	if request.method == 'GET':
		if "q" in request.GET:
			q = request.GET.get('q', '')
			pacientes = Paciente.objects.filter(nombrePersona__icontains=q)
			c = Consulta.objects.all()
	
	return render(request, 'verPaciente.html', {'pacientes': pacientes, 'expedientes': expedientes, 'noexp': noexp,})	

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

def VerConsulta(request, exp):
	consul = Consulta.objects.filter(expedientePac_id=exp)

	if request.method == 'GET':
		if "q" in request.GET:
			q = request.GET.get('q', '')
			consul = Consulta.objects.filter(fecha__icontains=q ).filter(expedientePac_id=exp)
			c = Consulta.objects.all() 
	return render(request, 'VerConsulta.html', {'consul' : consul,})

def VerExpediente(request):
	exp = Expediente.objects.all()
	pac = Paciente.objects.all()
	

	if request.method == 'GET':
		if "q" in request.GET:
			q = request.GET.get('q', '')
			exp = Expediente.objects.filter(NumExp__icontains=q)
			c = Expediente.objects.all() 
	return render(request, 'VerExpediente.html', {'exp' : exp,})


def RegistrarExpediente(request, pac):
	expedientes=Expediente.objects.all()
	cont = False
	blank= False


	if request.method == 'POST':
		exp = Expediente()
		pac = Paciente.objects.get(id=pac)
		exp.NumExp = request.POST['numExp']
		exp.paciente = pac
		if Expediente.objects.filter(NumExp=exp.NumExp).exists() == True:
			cont = True
			return render(request, 'crearExpediente.html',{'cont': cont,})
		elif exp.NumExp == "":
			blank = True
			return render(request, 'crearExpediente.html',{'cont': cont,'blank':blank,})
		else:
			exp.save()
			return HttpResponseRedirect('/ListaPaciente/')


	return render(request, 'crearExpediente.html',{'cont': cont,})


def RegistrarConsulta(request, exp):

	blank = False
	if request.method == 'POST':
		consulta= Consulta()
		consulta.fecha = request.POST['fecha']
		consulta.diag = request.POST['diag']
		consulta.expedientePac = Expediente.objects.get(id=exp)

		if consulta.fecha == "" :
			blank=True
			return render(request, 'RegistrarConsulta.html', {'blank': blank,})
		elif consulta.diag == "":
			blank=True
			return render(request, 'RegistrarConsulta.html', {'blank': blank,})
		else:
			consulta.save()
			return HttpResponseRedirect('/VerExpediente/')


	return render(request, 'RegistrarConsulta.html',)

