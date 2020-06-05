from django.shortcuts import render

from django.http import Http404

# Importamos el modelo
from .models import Mascota

# Creamos el controlador para la página inicial
def home(request):
    pets = Mascota.objects.all()
    return render(request, 'home.html',{
        'mascotas':pets,
    })

# Creamos el controlador para la página de detalle de mascota
def detalle_mascota(request, mascota_id):
    try:
        pet = Mascota.objects.get(id=mascota_id)
    except Mascota.DoesNotExist:
        raise Http404('Error desde proyectosbeta')

    return render(request, 'detalle_mascota.html',{
        'mascota':pet,
    })
