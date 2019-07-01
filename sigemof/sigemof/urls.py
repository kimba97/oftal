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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('RegistrarPaciente/', views.CreatePaciente.as_view(), name='RegistrarPaciente'),
    path('ListaPaciente/', views.ListPaciente.as_view(), name='ListaPaciente'),
    re_path(r'^Paciente/editar/(?P<id>\d+)', UpdatePaciente, name='EditarPaciente'),
    re_path(r'^Paciente/eliminar/(?P<id>\d+)', DeletePaciente, name='EliminarPaciente'),
]
