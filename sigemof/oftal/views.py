from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.urls import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import permission_required, login_required
from django.http.response import HttpResponseRedirect
from oftal.forms import *
from django.contrib.auth import authenticate, login
from datetime import datetime
import time
from django.conf import settings
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from django.views.generic import View

# Create your views here.


def index(request):
    return render(request, 'index.html')

def Base(request):
    return render(request, 'Base.html')

def inicio(request):
    return render(request, 'inicio.html')

@login_required
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
@permission_required('oftal.isDoctora')
def registrarAro(request):
    if request.method == 'POST':
        aro = Aro()
        aro.codigo = request.POST['codigo']
        aro.estado = "En Inventario"
        aro.color = request.POST['color']
        aro.marca = request.POST['marca']
        aro.tamano = request.POST['tamano']
#        lente.cantidad = request.POST['cantidad']
#        lente.precioCompra = request.POST['precioC']
        aro.save()
        return HttpResponseRedirect('/ListaAro/')
    return render(request, 'registrarAro.html',)

@login_required
def ListAro(request):
    aros = Aro.objects.all()
#    for p in lentes:
    if request.method == 'GET':
        if "q" in request.GET:
            q = request.GET.get('q', '')
            aros = Aro.objects.filter(codigo__icontains=q)
            c = Consulta.objects.all()

    return render(request, 'verAro.html', {'aros': aros, })

#class UpdateLente(UpdateView):
#    model = Lente
#    form_class = LenteForm
#    template_name = 'RegistrarLente.html'
#    success_url = '/ListaLente/'

@login_required
@permission_required('oftal.isDoctora')
def UpdateAro(request, id):
    aro = Aro.objects.get(id=id)
    if request.method == 'GET':
        form = AroForm(instance=aro)
    else:
        form = AroForm(request.POST, instance=aro)
        if form.is_valid():
            form.save()
        return redirect('ListaAro')
    return render(request, 'EditarAro.html', {'form': form})

@login_required
@permission_required('oftal.isDoctora')
def DeleteAro(request, id):
    aro = Aro.objects.get(id=id)
    if request.method == 'POST':
        aro.delete()
        return redirect('ListaAro')
    return render(request, 'EliminarAro.html', {'aro': aro})

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
@permission_required('oftal.isDoctora')
def DeletePaciente(request, id):
    paciente = Paciente.objects.get(id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('ListaPaciente')
    return render(request, 'EliminarPaciente.html', {'Paciente': paciente})

@login_required
@permission_required('oftal.isDoctora')
def VerConsulta(request, exp):
    consul = Consulta.objects.filter(expedientePac_id=exp)

    if request.method == 'GET':
        if "q" in request.GET:
            q = request.GET.get('q', '')
            consul = Consulta.objects.filter(fecha__icontains=q).filter(expedientePac_id=exp)
            c = Consulta.objects.all()
    return render(request, 'VerConsulta.html', {'consul': consul, })

@login_required
@permission_required('oftal.isDoctora')
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
@permission_required('oftal.isDoctora')
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
@permission_required('oftal.isDoctora')
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


def registrarLente(request):

    paci = Paciente.objects.all()
#        paciente = Paciente.objects.all()

    if request.method == 'POST':
        lente = Lente()
        ff=request.POST['paciente']
        lente.paciente = Paciente.objects.get(nombrePersona=ff)
        lente.estado = "laboratorio"
        lente.codigo = request.POST['codigo']
        lente.esfera = request.POST['esfera']
        lente.cilindro = request.POST['cilindro']
        lente.eje = request.POST['eje']
        lente.prisma = request.POST['prisma']
        lente.base = request.POST['base']
        lente.adicion = request.POST['adicion']
        lente.graduacion = request.POST['graduacion']
#        cristal.material = request.POST['material']
        lente.color = request.POST['color']


        lente.esferad = request.POST['esferad']
        lente.cilindrod = request.POST['cilindrod']
        lente.ejed = request.POST['ejed']
        lente.prismad = request.POST['prismad']
        lente.based = request.POST['based']
        lente.adiciond = request.POST['adiciond']
        lente.graduaciond = request.POST['graduaciond']
        #        cristal.material = request.POST['material']
        lente.colord = request.POST['colord']
#        cristal.marca = request.POST['marca']
#        cristal.cantidad = request.POST['cantidad']
#        cristal.precioCompra = request.POST['precioC']
        lente.save()
        return HttpResponseRedirect('/ListaLente/')
    return render(request, 'RegistrarLente.html',{'paci' : paci, })

@login_required
def verCita(request):
    c = Cita.objects.all()
    if request.method == 'GET':
        if "q" in request.GET:
            q = request.GET.get('q','')
            c = Cita.objects.filter(fecha__icontains=q)
    return render(request, 'verCita.html', {'c' : c, })

@login_required
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
@permission_required('oftal.isDoctora')
def UpdateLente(request, id):

    lent = Lente.objects.get(id=id)
    if request.method == 'POST':
        lent.codigo = request.POST['codigo']
        lent.esfera = request.POST['esfera']
        lent.cilindro = request.POST['cilindro']
        lent.eje = request.POST['eje']
        lent.prisma = request.POST['prisma']
        lent.base = request.POST['base']
        lent.adicion = request.POST['adicion']
        lent.graduacion = request.POST['graduacion']
        lent.color = request.POST['color']

        lent.esferad = request.POST['esferad']
        lent.cilindrod = request.POST['cilindrod']
        lent.ejed = request.POST['ejed']
        lent.prismad = request.POST['prismad']
        lent.based = request.POST['based']
        lent.adiciond = request.POST['adiciond']
        lent.graduaciond = request.POST['graduaciond']
        #        cristal.material = request.POST['material']
        lent.colord = request.POST['colord']
        lent.save()
        return HttpResponseRedirect('/ListaLente/')
    return render(request, 'EditarLente.html', {'lent': lent, })

#    if (lent):
#        lent.save()
#        return redirect('ListaLente')


#    if request.method == 'GET':
#        form = LenteForm(instance=lente)
#    else:
#        form = LenteForm(request.POST, instance=lente)
#        if form.is_valid():
#            form.save()

    return render(request, 'EditarLente.html', context)

@login_required
@permission_required('oftal.isDoctora')
def DeleteLente(request, id):
    lente = Lente.objects.get(id=id)
    if request.method == 'POST':
        lente.delete()
        return redirect('ListaLente')
    return render(request, 'EliminarLente.html', {'Lente': lente})

@login_required
def FacturaVenta(request):
    if request.method == 'POST':
        return render(request, 'FacturaVenta.html',{})

@login_required
@permission_required('oftal.isSecretaria')
def registrarCita(request, pac):
    paciente = Paciente.objects.get(id=pac)
    cita = Cita()
    now = datetime.now()
    val= True
    if request.method == 'POST':
        cita.fecha = request.POST['fecha']
        cita.horaI = request.POST['horaI']
        cita.horaF = request.POST['horaF']
        cita.estado = request.POST['estado']
        cita.paciCita = paciente
        fechaI = datetime.strptime(cita.fecha, '%Y-%m-%d')
        if now > fechaI:
            val = False
            return render(request, 'registrarCita.html', {'val': val })
        else:
            cita.save()
        return redirect('ListaPaciente')
    return render(request, 'registrarCita.html', {'Paciente': paciente, 'val': val})

@login_required
def verCitasP(request, pac):

    cits = Cita.objects.filter(paciCita=pac).order_by('fecha')
    return render(request, 'verCitasP.html', {'cits': cits, })

@login_required
@permission_required('oftal.isScretaria')
def editarEstado(request,id):
    cita = Cita.objects.get(id=id)
    if request.method == 'GET':
        form = CitaForm(instance=cita)
    else:
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/verCitasP/'+ str(cita.paciCita.id))
        #cita.estado = request.POST['estado']
        #cita.update()

    return render(request, 'editarEstado.html', {'form':form, })

@login_required
def registrarFacturaAro(request):
    aro =Aro.objects.all()
    pac =Paciente.objects.all()
    if request.method == 'POST':
        facturaAro = FacturaAro()

        aro = int(request.POST['aro'])
        ar = Aro.objects.get(id=aro)
        facturaAro.aro = ar

        p = int(request.POST['paciente'])
        facturaAro.paciente = Paciente.objects.get(id=p)

        ar.estado = "cancelado"

        facturaAro.descripcion = request.POST['descripcion']
        facturaAro.precio = request.POST['precio']
        facturaAro.cantidad = request.POST['cantidad']
        facturaAro.total = request.POST['total']
        facturaAro.save()
        ar.save()
        return HttpResponseRedirect('/verFacturaAro/')
    return render(request, 'registrarFacturaAro.html',{'aro': aro, 'pac': pac, })

@login_required
def verFacturaAro(request):
    fac = FacturaAro.objects.all()

    return render(request, 'verFacturaAro.html', {'fac' : fac, })

@login_required
def registrarFacturaVentaEntrada(request):
    per = Lente.objects.all()
    if request.method == 'POST':
        factura = FacturaVentaEntrada()
        #pacient = int(request.POST['paciente'])
        #paci = Paciente.objects.get(id=pacient)
#        paciente = Paciente.objects.all()
        #factura.paciente = paci
#        factura.paciente = request.POST['paciente']
        factura.codigoFactura = request.POST['codigo']
        factura.descripcion = request.POST['descripcion']

        lent = int(request.POST['paciente'])
        len = Lente.objects.get(codigo=lent)
        factura.lente = len
        print(5)
        print(factura.lente.paciente.nombrePersona)
        print(factura.lente.paciente.id)
        print(factura.lente.paciente)
        factura.paciente = factura.lente.paciente
        len.estado = "cancelado"

#        factura.lente = request.POST['lente']

        #ar = int(request.POST['aro'])
        #aros = Aro.objects.get(id=ar)
        #factura.aro = aros

#        factura.aro = request.POST['aro']
        factura.precioVenta = request.POST['precio']
        factura.cantidad = request.POST['cantidad']
        factura.total = request.POST['total']
        factura.save()
        len.save()
        return HttpResponseRedirect('/verFacturaVentaEntrada/')
    return render(request, 'registrarFacturaVentaEntrada.html', {'per' : per, })

@login_required
def verFacturaVentaEntrada(request):

    facEntrada = FacturaVentaEntrada.objects.all()
    return render(request, 'verFacturaVentaEntrada.html', {'facEntrada' : facEntrada, })


#def verFacturaVenta(request):

#    s = FacturaVenta.objects.all()
#    return render(request, 'verFacturaVenta.html', {'s' : s, })

#def verFacturaVenta(request):
#    fact = FacturaVenta.objects.all()
#    return render(request, 'verFacturaVenta.html', {'fact': fact, })
class ReportePersonasPDF(View):
    def cabecera(self,pdf):
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(200, 550, u"Consultorio Mèdico Oftalmològico: Dra. Lily de Chicas")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(300, 500, u"REPORTE DE LENTES")
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setPageSize((11*inch, 8.5*inch))
        self.cabecera(pdf)
        y=250
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf =buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


    def tabla(self,pdf,y):
        encabezados = ('Ojo', 'Paciente', 'Codigo', 'Estado', 'Esfera', 'Cilindro', 'Eje', 'Prisma', 'Base', 'Adicion', 'Graduacion', 'Color')
        detallesIzquierdo=[]
        detallesDerecho = []
        for lente in Lente.objects.all():
            detallesIzquierdo.append(('Izquierdo', lente.paciente.nombrePersona + lente.paciente.apellidoPersona, lente.codigo, lente.estado, lente.esfera, lente.cilindro, lente.eje, lente.prisma, lente.base, lente.adicion, lente.graduacion, lente.color))
            detallesIzquierdo.append(('Derecho', lente.paciente.nombrePersona + lente.paciente.apellidoPersona, '', lente.estado, lente.esferad, lente.cilindrod, lente.ejed, lente.prismad, lente.based, lente.adiciond, lente.graduaciond, lente.colord))
            detallesIzquierdo.append(('','','','','','','','','','','',''))
        detalleOrden = Table([encabezados] + detallesIzquierdo, colWidths=[0.7*inch, 2*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.8*inch, 0.7*inch, 0.7*inch, 0.7*inch, 0.9*inch, 0.9*inch])
        detalleOrden.setStyle(TableStyle([
            ('ALIGN',(0,0),(3,0),'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]))
        detalleOrden.wrapOn(pdf, 800, 600)
        detalleOrden.drawOn(pdf, 11, y)

class ReportePacientesPDF(View):
    def cabecera(self,pdf):
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(100, 700, u"Consultorio Mèdico Oftalmològico: Dra. Lily de Chicas")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 650, u"REPORTE DE PACIENTES")
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setPageSize((8.5*inch, 11*inch))
        self.cabecera(pdf)
        y=500
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf =buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


    def tabla(self,pdf,y):
        encabezados = ('Nombres', 'Apellidos', 'DUI', 'Edad', 'Sexo', 'Telefono', 'Correo')
        detalles = [(paciente.nombrePersona, paciente.apellidoPersona, paciente.dui, paciente.edad, paciente.sexo, paciente.telefono, paciente.correo) for paciente in Paciente.objects.all()]
        detalleOrden = Table([encabezados] + detalles, colWidths=[1.1*inch, 1.1*inch, 0.9*inch, 0.8*inch, 0.8*inch, 0.8*inch, 2*inch])
        detalleOrden.setStyle(TableStyle([
            ('ALIGN',(0,0),(3,0),'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]))
        detalleOrden.wrapOn(pdf, 800, 500)
        detalleOrden.drawOn(pdf, 50, y)


class ReporteExpedientesPDF(View):
    def cabecera(self,pdf):
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(110, 700, u"Consultorio Mèdico Oftalmològico: Dra. Lily de Chicas")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(210, 650, u"REPORTE DE EXPEDIENTES")
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setPageSize((8.5*inch, 11*inch))
        self.cabecera(pdf)
        y=570
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf =buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


    def tabla(self,pdf,y):
        encabezados = ('Numero de Expediente', 'Nombre', 'telefono', 'Correo')
        detallesIzquierdo = [(exp.NumExp, exp.paciente.nombrePersona + exp.paciente.apellidoPersona, exp.paciente.telefono, exp.paciente.correo) for exp in Expediente.objects.all()]
        detalleOrden = Table([encabezados] + detallesIzquierdo, colWidths=[1.6*inch, 2.5*inch, 1.8*inch, 2*inch])
        detalleOrden.setStyle(TableStyle([
            ('ALIGN',(0,0),(3,0),'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]))
        detalleOrden.wrapOn(pdf, 800, 500)
        detalleOrden.drawOn(pdf, 11, y)

class ReporteArosPDF(View):
    def cabecera(self,pdf):
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(110, 700, u"Consultorio Mèdico Oftalmològico: Dra. Lily de Chicas")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(210, 650, u"REPORTE DE AROS")
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setPageSize((8.5*inch, 11*inch))
        self.cabecera(pdf)
        y=400
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf =buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self,pdf,y):
        encabezados = ('Codigo', 'Estado', 'Color', 'Marca', 'Tamaño')
        detallesIzquierdo = [(aro.codigo, aro.estado, aro.color, aro.marca, aro.tamano) for aro in Aro.objects.all()]
        detalleOrden = Table([encabezados] + detallesIzquierdo, colWidths=[1.4*inch, 2*inch, 1.5*inch, 1.5*inch, 1.5*inch])
        detalleOrden.setStyle(TableStyle([
            ('ALIGN',(0,0),(3,0),'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]))
        detalleOrden.wrapOn(pdf, 800, 600)
        detalleOrden.drawOn(pdf, 11, 570)

class ReporteExpedientesPDF(View):
    def cabecera(self,pdf):
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(110, 700, u"Consultorio Mèdico Oftalmològico: Dra. Lily de Chicas")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(210, 650, u"REPORTE DE EXPEDIENTES")
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setPageSize((8.5*inch, 11*inch))
        self.cabecera(pdf)
        y=400
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf =buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self,pdf,y):
        encabezados = ('Numero de Expediente', 'Nombre', 'telefono', 'Correo')
        detallesIzquierdo = [(exp.NumExp, exp.paciente.nombrePersona + exp.paciente.apellidoPersona, exp.paciente.telefono, exp.paciente.correo) for exp in Expediente.objects.all()]
        detalleOrden = Table([encabezados] + detallesIzquierdo, colWidths=[1.6*inch, 2.5*inch, 1.8*inch, 2*inch])
        detalleOrden.setStyle(TableStyle([
            ('ALIGN',(0,0),(3,0),'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]))
        detalleOrden.wrapOn(pdf, 800, 600)
        detalleOrden.drawOn(pdf, 11, 570)

class ReporteSalidaLentesPDF(View):
    def cabecera(self,pdf):
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(110, 700, u"Consultorio Mèdico Oftalmològico: Dra. Lily de Chicas")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(210, 650, u"REPORTE SALIDAS DE LENTES")
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setPageSize((8.5*inch, 11*inch))
        self.cabecera(pdf)
        y=400
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf =buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self,pdf,y):
        encabezados = ('Paciente', 'Cod. Factura', 'Descripcion', 'lente', 'Precio Venta', 'Cantidad', 'Total')
        detallesIzquierdo = [(f.paciente.nombrePersona + f.paciente.apellidoPersona, f.codigoFactura, f.descripcion, f.lente, f.precioVenta, f.cantidad, f.total) for f in FacturaVentaEntrada.objects.all()]
        detalleOrden = Table([encabezados] + detallesIzquierdo, colWidths=[2.1*inch, 0.9*inch, 1.8*inch, 0.7*inch, 1*inch, 0.65*inch, 1.1*inch])
        detalleOrden.setStyle(TableStyle([
            ('ALIGN',(0,0),(3,0),'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]))
        detalleOrden.wrapOn(pdf, 800, 600)
        detalleOrden.drawOn(pdf, 11, 570)

class ReporteSArosPDF(View):
    def cabecera(self,pdf):
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(110, 700, u"Consultorio Mèdico Oftalmològico: Dra. Lily de Chicas")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(210, 650, u"REPORTE SALIDE AROS")
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.setPageSize((8.5*inch, 11*inch))
        self.cabecera(pdf)
        y=400
        self.tablaaro(pdf, 400)
        pdf.showPage()
        pdf.save()
        pdf =buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tablaaro(self,pdf,y):
        encabezados = ('Nombre Paciente', 'Cod. Aro', 'Descripcion')
        detallesIzquierdo = [(f.paciente.nombrePersona + f.paciente.apellidoPersona, f.aro, f.descripcion) for f in FacturaAro.objects.all()]
        detalleOrden = Table([encabezados] + detallesIzquierdo, colWidths=[2.1*inch, 0.9*inch, 1.8*inch])
        detalleOrden.setStyle(TableStyle([
            ('ALIGN',(0,0),(3,0),'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]))
        detalleOrden.wrapOn(pdf, 800, 600)
        detalleOrden.drawOn(pdf, 11, 570)
