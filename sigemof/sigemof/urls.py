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
from django.urls import path, re_path
from oftal import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^calendario', calendario, name='calendario'),
    url(r'^registrarPaciente/', registrarPaciente, name='registrarPaciente'),
    url(r'^registrarLente/', registrarLente, name='registrarLente'),
    url(r'^registrarCristal/', registrarCristal, name='registrarCristal'),

#    path('ListaPaciente/', views.ListPaciente.as_view(), name='ListaPaciente'),
    url(r'^ListaPaciente/', ListPaciente, name='ListaPaciente'),
    url(r'^ListaLente/', ListLente, name='ListaLente'),
    url(r'^ListaCristal/', ListCristal, name='ListaCristal'),

    re_path(r'^Paciente/editar/(?P<id>\d+)', UpdatePaciente, name='EditarPaciente'),
    re_path(r'^Lente/editar/(?P<id>\d+)', UpdateLente, name='EditarLente'),
    re_path(r'^Cristal/editar/(?P<id>\d+)', UpdateCristal, name='EditarCristal'),

    re_path(r'^Paciente/eliminar/(?P<id>\d+)', DeletePaciente, name='EliminarPaciente'),
    re_path(r'^Lente/eliminar/(?P<id>\d+)', DeleteLente, name='EliminarLente'),
    re_path(r'^Cristal/eliminar/(?P<id>\d+)', DeleteCristal, name='EliminarCristal'),

    #path('', views.index, name='index'),
    url(r"^VerConsulta/(?P<exp>[^/]+)/$", VerConsulta, name='VerConsulta'),
    url(r'^VerExpediente/', VerExpediente, name='VerExpediente'),
    url(r"^RegistrarExpediente/(?P<pac>[^/]+)/$", RegistrarExpediente, name='RegistrarExpediente'),
    url(r"^RegistrarConsulta/(?P<exp>[^/]+)/$", RegistrarConsulta, name='RegistrarConsulta'),
    #url(r'^login/$', 'django.contrib.auth.views.login'),
    #url(r'^logout/$',   'django.contrib.auth.views.logout', {'next_page': '/index/'}),
    path('login/', auth_views.LoginView.as_view(template_name = 'index.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'index.html'), name = 'logout'),
    url(r'^', inicio, name='inicio'),

    url(r'^FacturaVenta/', FacturaVenta, name='FacturaVenta'),
]