from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno
from .forms import AlumnoForm
from datetime import date
from django.db.models.functions import ExtractYear
from django.db.models import Count

def alumno_list_view(request):
    alumnos = Alumno.objects.all()
    return render(request, 'formularioAlumnos/alumno_list.html', {'alumnos': alumnos})

def alumno_create_view(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el alumno en la base de datos
            return redirect('alumno_list')  # Redirige a la lista de alumnos
    else:
        form = AlumnoForm()
    return render(request, 'formularioAlumnos/alumno_form.html', {'form': form})


def alumno_update_view(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    form = AlumnoForm(request.POST or None, instance=alumno)
    if form.is_valid():
        form.save()
        return redirect('alumno_list')
    return render(request, 'formularioAlumnos/alumno_form.html', {'form': form})

def alumno_delete_view(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumno_list')
    return render(request, 'formularioAlumnos/alumno_confirm_delete.html', {'alumno': alumno})

def estadisticas_alumnos_view(request):
    # Calcular la edad de cada alumno y contar las ocurrencias
    estadisticas = {}
    for alumno in Alumno.objects.all():
        edad = date.today().year - alumno.fechaNacimiento.year
        estadisticas[edad] = estadisticas.get(edad, 0) + 1

    return render(request, 'formularioAlumnos/estadisticas_alumnos.html', {'estadisticas': estadisticas})