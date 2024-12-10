from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.

class ClasePunto(models.Model):
    comuna = models.CharField(max_length=50)
    calle = models.CharField(max_length =50)
    numero = models.CharField(max_length = 15)

class ClaseMuni(models.Model):
    comuna = models.CharField(max_length=50)
    

class ClaseIncentivo(models.Model):
    material = models.CharField(max_length=50)
    valorPorKilo = models.CharField(max_length =50)
    promocion = models.CharField(max_length = 128)


class ClaseCuentaB(models.Model):
    NumeroCuenta = models.CharField(max_length=50)
    Banco = models.CharField(max_length =50)
    Nombre = models.CharField(max_length=50)
    Rut= models.CharField(max_length =50)
    Correo= models.CharField(max_length = 128)
    
class ClaseContacto(models.Model):
    Telefono = models.CharField(max_length=50)
    Correo = models.CharField(max_length =50)
    def __str__(self):
        return f"Contacto {self.id} de {self.usuario.username}"

class ClaseLogin(models.Model):
    username = models.EmailField(max_length =50, unique= True)
    password = models.CharField(max_length=128)
    recontrasena = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
