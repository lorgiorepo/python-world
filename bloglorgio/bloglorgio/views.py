from docutils.nodes import entry

__author__ = 'lorgio'
from django.shortcuts import render_to_response

from bloglorgio.models import Articulos

def home(request):
    contenido = {
        'titulo' : 'Mi primer gran articulo',
        'autor' : 'Carlos Picca',
        'dia' : '19 de Julio de 2013',
        'contenido' : 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam cursus tempus dui, ut vulputate nisl eleifend eget. Aenean justo felis, dapibus quis vulputate at, porta et dolor. Praesent enim libero, malesuada nec vestibulum vitae, fermentum nec ligula. Etiam eget convallis turpis. Donec non sem justo.',
    }
    entradas = Articulos.objects.all()[:10]
    return render_to_response('index.html', {'articulos': entradas})
