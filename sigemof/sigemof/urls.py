"""sigemof URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from oftal.views import *
from django.urls import path, re_path,include
from oftal import views
from django.contrib.auth import views as auth_views
#from django_private_chat import urls as django_private_chat_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^reporte_personas_pdf/$',login_required(ReportePersonasPDF.as_view()), name="reporte_personas_pdf"),
    url(r'^reporte_pacientes_pdf/$',login_required(ReportePacientesPDF.as_view()), name="reporte_pacientes_pdf"),
    url(r'^reporte_aros_pdf/$',login_required(ReporteArosPDF.as_view()), name="reporte_aros_pdf"),
    url(r'^reporte_expedientes_pdf/$',login_required(ReporteExpedientesPDF.as_view()), name="reporte_expedientes_pdf"),
    url(r'^reporte_salidalentes_pdf/$',login_required(ReporteSalidaLentesPDF.as_view()), name="reporte_salidalentes_pdf"),
    url(r'^reporte_saros_pdf/$',login_required(ReporteSArosPDF.as_view()), name="reporte_saros_pdf"),
    #url(r'^reporte_aros_pdf/$',login_required(ReporteArosPDF.as_view()), name="reporte_aros_pdf"),
    url(r'^reporte_expedientes_pdf/$',login_required(ReporteExpedientesPDF.as_view()), name="reporte_expedientes_pdf"),
    #url(r'^', include('django_private_chat.urls')),
    url(r'^calendario', calendario, name='calendario'),
    url(r'^registrarPaciente/', registrarPaciente, name='registrarPaciente'),
    url(r'^registrarAro/', registrarAro, name='registrarAro'),
    url(r'^registrarLente/', registrarLente, name='registrarLente'),
    url(r'^verCita/', verCita, name='verCita'),
    url(r'^registrarFacturaAro/', registrarFacturaAro, name='registrarFacturaAro'),
    url(r'^registrarFacturaVentaEntrada/', registrarFacturaVentaEntrada, name='registrarFacturaVentaEntrada'),
    url(r'^verFacturaAro/', verFacturaAro, name='verFacturaAro'),
    url(r'^verFacturaVentaEntrada/', verFacturaVentaEntrada, name='verFacturaVentaEntrada'),

#    path('ListaPaciente/', views.ListPaciente.as_view(), name='ListaPaciente'),
    url(r'^ListaPaciente/', ListPaciente, name='ListaPaciente'),
    url(r'^ListaAro/', ListAro, name='ListaAro'),
    url(r'^ListaLente/', ListLente, name='ListaLente'),


    re_path(r'^Paciente/editar/(?P<id>\d+)', UpdatePaciente, name='EditarPaciente'),
    re_path(r'^Aro/editar/(?P<id>\d+)', UpdateAro, name='EditarAro'),
    re_path(r'^Lente/editar/(?P<id>\d+)', UpdateLente, name='EditarLente'),

    re_path(r'^Paciente/eliminar/(?P<id>\d+)', DeletePaciente, name='EliminarPaciente'),
    re_path(r'^Aro/eliminar/(?P<id>\d+)', DeleteAro, name='EliminarAro'),
    re_path(r'^Lente/eliminar/(?P<id>\d+)', DeleteLente, name='EliminarLente'),
    re_path(r'^editarEstado/(?P<id>\d+)', editarEstado, name='editarEstado'),
    re_path(r"^verCitasP/(?P<pac>\d+)", verCitasP, name='verCitasP'),
    #path('', views.index, name='index'),
    url(r"^VerConsulta/(?P<exp>[^/]+)/$", VerConsulta, name='VerConsulta'),


    url(r'^VerExpediente/', VerExpediente, name='VerExpediente'),
    url(r"^RegistrarExpediente/(?P<pac>[^/]+)/$", RegistrarExpediente, name='RegistrarExpediente'),

    url(r"^RegistrarConsulta/(?P<exp>[^/]+)/$", RegistrarConsulta, name='RegistrarConsulta'),
    url(r"^registrarCita/(?P<pac>[^/]+)/$", registrarCita, name='registrarCita'),
    #url(r'^login/$', 'django.contrib.auth.views.login'),
    #url(r'^logout/$',   'django.contrib.auth.views.logout', {'next_page': '/index/'}),
    path('login/', auth_views.LoginView.as_view(template_name = 'index.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'index.html'), name = 'logout'),
    url(r'^', inicio, name='inicio'),

]