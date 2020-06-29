from django.shortcuts import render,get_object_or_404, redirect

from aula.service import *

def index(request):
    template_name = 'index.html'
    context = {}
    return render(request,template_name, context)


def home(request):
    template_name = 'home.html'
    context = {}
    return render(request,template_name, context)


def catalogo(request):
    template_name = 'catalogo.html'
    context = {'aulas': get_aulas()}
    return render(request,template_name, context)
