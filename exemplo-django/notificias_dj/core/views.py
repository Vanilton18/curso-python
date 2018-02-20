from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

#from models import Noticias
#from core.models import Noticias
from .models import Noticia

def inicio(request):
    contexto = {
        'titulo': 'Notícias',
        'noticias': Noticia.objects.all()
    }
    return render(request, 'index.html', contexto)

def noticia(request, pk):
    #noticia = Noticia.objects.get(pk=pk)
    noticia = get_object_or_404(Noticia, pk=pk)
    contexto = {
        'titulo': noticia.titulo,
        'noticia': noticia
    }

    return render(request, 'detalhe_noticia.html', contexto)