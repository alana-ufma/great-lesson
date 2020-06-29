
from django.shortcuts import render,get_object_or_404, redirect
from aula.models import *
from aula.forms import *
# import aula.entities.aula as entidade
from .service import *
from .forms import AulaForm
from recurso.forms import RecursoForm
from django.template.defaultfilters import slugify


def index(request):
    template_name = 'aulas/index.html'
    aulas = Aula.objects.all().filter(criador=request.user)
    context = {'aulas':aulas}
    return render(request,template_name, context)

def exemplo_aula(request):
    template_name = 'aulas/exemplo.html'
    aulas = Aula.objects.all()
    context = {'aulas':aulas}
    return render(request,template_name, context)

#
def listar_aulas(request):
    aulas =  Aula.objects.all().filter(criador=request.user)
    context = {'aulas': aulas}
    template_name = 'aulas/index.html'
    return render(request,template_name, context)
#
#


def preview_aula(request, slug):
    aula = get_aula_by_slug(slug)
    context = {
        'aula': aula
    }

    template_name = 'aulas/preview.html'
    return render(request,template_name, context)

def buscar_aula(request, slug):
    aula = get_aula_by_slug(slug)
    form_recurso = RecursoForm()
    form_aula = AulaForm(instance=aula)

    if 'active_tab' in request.session:
        active_tab = request.session['active_tab']
    else:
        active_tab = 'gerais'


    context = {
        'aula': aula,
        'form_recurso': form_recurso,
        'form_aula': form_aula,
        'active_tab': active_tab,
        }
    template_name = 'aulas/view.html'
    return render(request,template_name, context)

#
# def remover_aula(request, id):
#     aula = get_aula(id)
#     if request.method == "POST":
#
#         remove_aula(aula)
#         return redirect('aula:listar_aulas')
#
#     context = {'aula': aula }
#     template_name = 'aulas/delete.html'
#     return render(request,template_name, context)
#
#
def inserir_aula(request):
    if request.method == "POST":
        form_aula = AulaForm(request.POST, request.FILES or None)

        if form_aula.is_valid():
            aula = form_aula.save()
            aula.slug = slugify(aula.titulo)
            aula.save()

            return redirect('aula:listar_aulas')
    else:
        form_aula = AulaForm()

    context = { 'form_aula': form_aula }
    template_name = 'aulas/form.html'
    return render(request,template_name, context)
#
#
def editar_aula(request, id):
    aula_antigo = get_aula(id)
    form_aula = AulaForm(request.POST or None, instance = aula_antigo)

    if form_aula.is_valid():
        form_aula.save()
        # titulo  = form_aula.cleaned_data["titulo"]
        # descricao  = form_aula.cleaned_data["descricao"]
        # leituras  = form_aula.cleaned_data["leituras"]
        # audios  = form_aula.cleaned_data["audios"]
        # demos  = form_aula.cleaned_data["demos"]
        # videos  = form_aula.cleaned_data["videos"]
        # ensinos  = form_aula.cleaned_data["ensinos"]
        # praticas  = form_aula.cleaned_data["praticas"]
        #
        # aula_atualizado = aula.Aula(titulo=titulo, descricao=descricao, leituras=leituras, audios=audios, demos=demos, videos=videos, ensinos=ensinos, praticas=praticas)
        # edit_aula(aula_antigo, aula_atualizado)

        return redirect('aula:buscar_aula', aula_antigo.slug)


    context = { 'form_aula': form_aula, 'aula':aula_antigo }
    template_name = 'aulas/form.html'
    return render(request,template_name, context)
