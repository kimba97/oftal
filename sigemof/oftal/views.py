from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.urls import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import permission_required
from django.http.response import HttpResponseRedirect
from oftal.forms import *
from django.contrib.auth import authenticate, login
from datetime import datetime
import time
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Base(request):
    return render(request, 'Base.html')

def inicio(request):
    return render(request, 'inicio.html')

def calendario(request):
    return render(request, 'calendario.html')

@login_required
def registrarPaciente(request):
    if request.method == 'POST':
        pacientes = Paciente()
        pacientes.nombrePersona = request.POST['paci']
        pacientes.apellidoPersona = request.POST['apellido']
        pacientes.dui = request.POST['dui']
        pacientes.direccion = request.POST['direccion']
        pacientes.telefono = request.POST['tel']
        pacientes.fechaNac = request.POST['naci']
        dati = datetime.now()
        fechaN = datetime.strptime(pacientes.fechaNac, '%Y-%m-%d')
        pacientes.edad = (dati.year - fechaN.year)
        print(pacientes.edad)
        pacientes.sexo = request.POST['sexo']
        pacientes.correo = request.POST['correo']
        pacientes.nombrePadre = request.POST['nameP']
        pacientes.nombreMadre = request.POST['nameM']
        pacientes.remitente = request.POST['nameR']
        pacientes.save()
        return HttpResponseRedirect('/ListaPaciente/')
    return render(request, 'RegistrarPaciente.html', )

@login_required
def registrarLente(request):
    if request.method == 'POST':
        lente = Lente()
        lente.codigo = request.POST['codigo']
        lente.color = request.POST['color']
        lente.marca = request.POST['marca']
        lente.tamano = request.POST['tamano']
#        lente.cantidad = request.POST['cantidad']
#        lente.precioCompra = request.POST['precioC']
        lente.save()
        return HttpResponseRedirect('/ListaLente/')
    return render(request, 'registrarLente.html',)


def ListLente(request):
    lentes = Lente.objects.all()
#    for p in lentes:
    if request.method == 'GET':
        if "q" in request.GET:
            q = request.GET.get('q', '')
            lentes = Lente.objects.filter(codigo__icontains=q)
            c = Consulta.objects.all()

    return render(request, 'verLente.html', {'lentes': lentes, })

#class UpdateLente(UpdateView):
#    model = Lente
#    form_class = LenteForm
#    template_name = 'RegistrarLente.html'
#    success_url = '/ListaLente/'
@login_required
def UpdateLente(request, id):
    lente = Lente.objects.get(id=id)
    if request.method == 'GET':
        form = LenteForm(instance=lente)
    else:
        form = LenteForm(request.POST, instance=lente)
        if form.is_valid():
            form.save()
        return redirect('ListaLente')
    return render(request, 'EditarLente.html', {'form': form})
@login_required
def DeleteLente(request, id):
    lente = Lente.objects.get(id=id)
    if request.method == 'POST':
        lente.delete()
        return redirect('ListaLente')
    return render(request, 'EliminarLente.html', {'Lente': lente})
@login_required
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

    return render(request, 'verPaciente.html', {'pacientes': pacientes, 'expedientes': expedientes, 'noexp': noexp, })

#class UpdatePaciente(UpdateView):
 #   model = Paciente
  #  form_class = PacienteForm
   # template_name = 'RegistrarPaciente.html'
    #success_url = '/ListaPaciente/'
@login_required
def UpdatePaciente(request, id):
    paciente = Paciente.objects.get(id=id)
    if request.method == 'GET':
        form = PacienteForm(instance=paciente)
    else:
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
        return redirect('ListaPaciente')
    return render(request, 'EditarPaciente.html', {'form': form})

@login_required
def DeletePaciente(request, id):
    paciente = Paciente.objects.get(id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('ListaPaciente')
    return render(request, 'EliminarPaciente.html', {'Paciente': paciente})

@login_required
def VerConsulta(request, exp):
    consul = Consulta.objects.filter(expedientePac_id=exp)

    if request.method == 'GET':
        if "q" in request.GET:
            q = request.GET.get('q', '')
            consul = Consulta.objects.filter(fecha__icontains=q).filter(expedientePac_id=exp)
            c = Consulta.objects.all()
    return render(request, 'VerConsulta.html', {'consul': consul, })

@login_required
def VerExpediente(request):
    exp = Expediente.objects.all()
    pac = Paciente.objects.all()

    if request.method == 'GET':
        if "q" in request.GET:
            q = request.GET.get('q', '')
            exp = Expediente.objects.filter(NumExp__icontains=q)
            c = Expediente.objects.all()
    return render(request, 'VerExpediente.html', {'exp': exp, })

@login_required
def RegistrarExpediente(request, pac):
    expedientes = Expediente.objects.all()
    cont = False
    blank = False

    if request.method == 'GET':
        exp = Expediente()
        paci = Paciente.objects.get(id=pac)
        letra = paci.apellidoPersona[0]
        sex = paci.sexo[0]
        codigo = sex + letra
        co = paci.id
        ram = str(co).zfill(4)
        numm = str(ram)
        num = codigo + numm
        print(num)


        exp.NumExp = num
        exp.paciente = paci
        if Expediente.objects.filter(NumExp=exp.NumExp).exists() == True:
            cont = True
            return render(request, 'crearExpediente.html', {'cont': cont, })
        elif exp.NumExp == "":
            blank = True
            return render(request, 'crearExpediente.html', {'cont': cont, 'blank': blank, })
        else:
            exp.save()
            return HttpResponseRedirect('/VerExpediente/')

    return render(request, 'crearExpediente.html', {'cont': cont,})

@login_required
def RegistrarConsulta(request, exp):
    blank = False
    if request.method == 'POST':
        consulta = Consulta()
        consulta.fecha = request.POST['fecha']
        consulta.diag = request.POST['diag']
        consulta.expedientePac = Expediente.objects.get(id=exp)

        if consulta.fecha == "":
            blank = True
            return render(request, 'RegistrarConsulta.html', {'blank': blank, })
        elif consulta.diag == "":
            blank = True
            return render(request, 'RegistrarConsulta.html', {'blank': blank, })
        else:
            consulta.save()
            return HttpResponseRedirect('/VerExpediente/')

    return render(request, 'RegistrarConsulta.html', )

























@login_required
def registrarCristal(request):
    if request.method == 'POST':
        cristal = Cristal()
        cristal.codigo = request.POST['codigo']
        cristal.esfera = request.POST['esfera']
        cristal.cilindro = request.POST['cilindro']
        cristal.eje = request.POST['eje']
        cristal.prisma = request.POST['prisma']
        cristal.base = request.POST['base']
        cristal.adicion = request.POST['adicion']
        cristal.graduacion = request.POST['graduacion']
#        cristal.material = request.POST['material']
        cristal.color = request.POST['color']
#        cristal.marca = request.POST['marca']
#        cristal.cantidad = request.POST['cantidad']
#        cristal.precioCompra = request.POST['precioC']
        cristal.save()
        return HttpResponseRedirect('/ListaCristal/')
    return render(request, 'registrarCristal.html',)

def ListCristal(request):
    cristals = Cristal.objects.all()
#    for p in lentes:
    if request.method == 'GET':
        if "q" in request.GET:
            q = request.GET.get('q', '')
            cristals = Cristal.objects.filter(codigo__icontains=q)
            c = Consulta.objects.all()

    return render(request, 'verCristal.html', {'cristals': cristals, })

#class UpdateLente(UpdateView):
#    model = Lente
#    form_class = LenteForm
#    template_name = 'RegistrarLente.html'
#    success_url = '/ListaLente/'
@login_required
def UpdateCristal(request, id):
    cristal = Cristal.objects.get(id=id)
    if request.method == 'GET':
        form = CristalForm(instance=cristal)
    else:
        form = CristalForm(request.POST, instance=cristal)
        if form.is_valid():
            form.save()
        return redirect('ListaCristal')
    return render(request, 'EditarCristal.html', {'form': form})
@login_required
def DeleteCristal(request, id):
    cristal = Cristal.objects.get(id=id)
    if request.method == 'POST':
        cristal.delete()
        return redirect('ListaCristal')
    return render(request, 'EliminarCristal.html', {'Cristal': cristal})


def FacturaVenta(request):
    if request.method == 'POST':
        return render(request, 'FacturaVenta.html',{})

