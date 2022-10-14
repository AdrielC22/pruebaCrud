from doctest import ELLIPSIS_MARKER
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Tarea, Actividad
from .forms import ActividadForm, TareaForm

def home(request):
    tareas = Tarea.objects.all()
    actividades = Actividad.objects.all()
    context = {'tareas':tareas}
    contexdos={'actividades': actividades}
    return render(request, 'todo/home.html', context)
'''
def actividad(request):
    actividades = Actividad.objects.all()
    context ={'actividades':actividades}
    return render(request, 'todo/home.html', context)
'''

# Create your views here.
def agregar(request):
    if request.method =="POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    context ={'form': form}
    return render (request, 'todo/agregar.html', context)

def agregaractividad(request):
    if request.method =="POST":
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ActividadForm()
    context={'form':form}
    return render (request, 'todo/agregaractividad.html',context)


def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect("home")

def eliminaractividad(request, actividad_id):
    actividad = Actividad.objects.get(id=actividad_id)
    actividad.delete()
    return redirect("home")

def editar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance= tarea)
        if form.is_valid ():
            form.save()
            return redirect ("home")
    else:
        form = TareaForm(instance=tarea)
    
    context = {"form": form}
    return render(request, "todo/editar.html",context)

def editaractividad(request, actividad_id):
    actividad = Actividad.objects.get(id=actividad_id)
    if request.method == "POST":
        form = ActividadForm(request.POST, instance= actividad)
        if form.is_valid ():
            form.save()
            return redirect ("home")
    else:
        form = ActividadForm(instance=actividad)
    
    context = {"form": form}
    return render(request, "todo/editaractividad.html",context)
