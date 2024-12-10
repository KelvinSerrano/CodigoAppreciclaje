"""
URL configuration for ReciclajeBase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from ReciclajeApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('puntos2/', views.Recicla_2),
    path('agregar/', views.agregarCuenta),
    path('incentivos/', views.Incentivos_1),
    path('incentivos2/',views.Incentivos_2),
    path('cuenta/', views.RC_1),
    path('', views.index),
    path('eliminarAlumno/<int:id>', views.eliminarAlumno),
    path('actualizarAlumno/<int:id>', views.actualizarAlumno),
    path('eliminarContacto/<int:id>', views.eliminarContacto),
    path('actualizarContacto/<int:id>', views.actualizarContacto),
    path('agregarCon/', views.agregarContacto),
    path('contacto/', views.RCon),
    path('muni/', views.Muni),
    path('muni2/',views.Muni2),
    path('login/', views.login_view, name='login'),
    path('accesoLogin/acceso/', views.crearCuenta, name='crear_cuenta'),
    path('accesoLogin/',views.AccesoLogin, name='accesoLogin'),
    path('puntos/', views.Recicla_1, name='puntos'),  # Asegúrate de tener esta vista también

]

