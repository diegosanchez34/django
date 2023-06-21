from django.shortcuts import render

from .models import Genero, Alumno

# Create your views here.

def index(request):
    alumnos=Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/index.html', context)

def crud(request):
    alumnos=Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/listado.html', context)

def AgregarAlumno(request):
    if request.method is not "POST":    
        generos=Genero.objects.all()
        context={"generos":generos,"mensaje":"mensaje de prueba"}
        return render(request, 'alumnos/agregar.html', context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        paterno = request.POST["paterno"]
        materno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        celular = request.POST["celular"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]

        objGenero = Genero.objects.get(id_genero = genero)
        objAlumno = Alumno.objects.create(  rut=rut,
                                            nombre=nombre,
                                            apellido_paterno=paterno,
                                            apellido_materno=materno,
                                            fecha_nacimiento=fechaNac,
                                            id_genero=objGenero,
                                            telefono=celular,
                                            email=email,
                                            direccion=direccion,
                                            activo=1)
        obj.save()
        context={"mensaje":"Ok, datos grabados..."}
        return render(request, 'alumnos/agregar.html', context)

def EliminarAlumno(request):
    context={}
    return render(request, 'alumnos/eliminar.html', context)

def ModificarAlumno(request):
    context={}
    return render(request, 'alumnos/modificar.html', context)

