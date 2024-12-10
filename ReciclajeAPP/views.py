from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from ReciclajeApp.models import ClasePunto
from ReciclajeApp.models import ClaseIncentivo
from ReciclajeApp.models import ClaseMuni
from ReciclajeApp.models import ClaseCuentaB
from ReciclajeApp.forms import FormCuentaB
from ReciclajeApp.models import ClaseContacto
from ReciclajeApp.models import ClaseLogin
from ReciclajeApp.forms import FormContacto
from ReciclajeApp.forms import FormLogin
from ReciclajeApp.forms import LoginForm
from django.contrib.auth.hashers import check_password, make_password

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import FormLogin  # Si tienes un formulario personalizado para login
# Create your views here.
def eliminarAlumno(request, id):
    c= ClaseCuentaB.objects.get(id=id)
    c.delete()
    return redirect('/cuenta')

def actualizarAlumno(request, id):
    c=ClaseCuentaB.objects.get(id=id)
    form= FormCuentaB(instance=c)
    if request.method =='POST' :
        form = FormCuentaB(request.POST, instance=c)
        if form.is_valid() :
            form.save()
        return RC_1(request)
    data= {'form': form}
    return render(request,'editar.html', data)

def eliminarContacto(request, id):
    c= ClaseContacto.objects.get(id=id)
    c.delete()
    return redirect('/contacto')

def actualizarContacto(request, id):
    c=ClaseContacto.objects.get(id=id)
    form= FormContacto(instance=c)
    if request.method =='POST' :
        form = FormContacto(request.POST, instance=c)
        if form.is_valid() :
            form.save()
        return RCon(request)
    data= {'form': form}
    return render(request,'editarCon.html', data)


def RCon(request):
    co = ClaseContacto.objects.all()
    data = {'co': co}
    return render (request, 'vercontacto.html', data)

def agregarContacto(request):
    form= FormContacto()
    if request.method =='POST' :
        form = FormContacto(request.POST)
        if form.is_valid() :
            form.save()
    data= {'form': form}
    return render(request,'CONTACTO.HTML', data)


def Recicla_1(request):
    puntos = ClasePunto.objects.all()
    data = {'puntos': puntos}
    return render (request, 'TemplateRecicla.html', data)

def Recicla_2(request):
    puntos = ClasePunto.objects.all()
    data = {'puntos': puntos}
    return render (request, 'PUNTORECICLAJE2.html', data)


def RC_1(request):
    cu = ClaseCuentaB.objects.all()
    data = {'cu': cu}
    return render (request, 'vercuenta.html', data)



def Incentivos_1(request):
    incentivos = ClaseIncentivo.objects.all()
    data = {'incentivos': incentivos}
    return render (request, 'TemplateIncentivos.html', data)

def Incentivos_2(request):
    incentivos = ClaseIncentivo.objects.all()
    data = {'incentivos': incentivos}
    return render (request, 'incentivos2.html', data)

def index(request):
    return render(request, 'index.html')
    
def agregarCuenta(request):
    form= FormCuentaB()
    if request.method =='POST' :
        form = FormCuentaB(request.POST)
        if form.is_valid() :
            form.save()
    data= {'form': form}
    return render(request,'CUENTA.HTML', data)

def Muni(request):
    muni = ClaseMuni.objects.all()
    data = {'muni': muni}
    return render (request, 'TemplateMuni.html', data)

def Muni2(request):
    muni = ClaseMuni.objects.all()
    data = {'muni': muni}
    return render (request, 'municipalidad2.html', data)

# Vista para mostrar la página de login
def login_view(request):
    login = ClaseLogin.objects.all()  # Esto parece innecesario, puedes eliminarlo si no es relevante
    data = {'login': login}
    return render(request, 'inicio sesion.html', data)

# Vista para procesar el acceso del usuario

def AccesoLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = ClaseLogin.objects.get(username=username)  # Busca el usuario
            
            # Verifica si la contraseña ingresada es correcta
            if check_password(password, user.password):
                # Si la contraseña es correcta, inicia sesión
                request.session['user_id'] = user.id
                messages.success(request, 'Inicio de sesión exitoso')
                return redirect('puntos')  # O la vista a la que desees redirigir
            else:
                messages.error(request, 'Contraseña incorrecta')
        except ClaseLogin.DoesNotExist:
            messages.error(request, 'Correo electrónico no encontrado')

    return render(request, 'inicio sesion.html')

# Vista para crear una nueva cuenta
# Crear un nuevo usuario con contraseña encriptada
def crearCuenta(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Encriptar la contraseña antes de guardarla
        password_hash = make_password(password)
        
        # Crear el usuario con la contraseña encriptada
        user = ClaseLogin(username=username, password=password_hash)
        user.save()  # Guardar el usuario en la base de datos
        
        messages.success(request, "Cuenta creada con éxito")
        return redirect('login')  # Redirigir al login o donde necesites

    return render(request, 'crearCuenta.html')