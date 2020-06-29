from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages, auth

from .models import *
# Create your views here.
from recurso.service import *
from recurso.forms import *
from aula.service import *

def listar(request):
    template_name = 'recursos/index.html'
    recursos = Recurso.objects.all()
    context = {'recursos': recursos}
    return render(request,template_name, context)

def salvar_recurso_aula(request, id):
    aula = get_aula(id)

    print('aqui 1')
    if request.method == "POST":
        print('aqui 2')
        form_recurso = RecursoForm(request.POST, request.FILES or None)
        if form_recurso.is_valid():
            print('aqui 3')
            # recurso = form_recurso.save(commit=False)
            print(request.POST['tipo'])
            tipo  = request.POST['tipo']
            nome  = form_recurso.cleaned_data["nome"]
            descricao  = form_recurso.cleaned_data["descricao"]
            url  = form_recurso.cleaned_data["url"]
            arquivo  = form_recurso.cleaned_data["arquivo"]

            recurso_novo = Recurso(nome=nome, descricao=descricao, url=url, arquivo=arquivo)
            recurso = add_recurso(recurso_novo)

            if tipo == '1':
                aula.leituras.add(recurso) #lendo 10%
            elif tipo == '2':
                aula.audios.add(recurso) #escutando 20%
            elif tipo == '3':
                aula.demos.add(recurso) # vendo 30%
            elif tipo == '4':
                aula.videos.add(recurso) # vendo e ouvindo 50%
            elif tipo == '5':
                aula.discussoes.add(recurso) #discutindo 70%
            elif tipo == '6':
                aula.praticas.add(recurso) # fazendo 80%
            elif tipo == '7':
                aula.ensinos.add(recurso) # ensinando

            #     anamnese.perguntas_negativas.add(recurso)
            # elif tipo == 3:
            #     anamnese.perguntas_neutras.add(recurso)

            messages.success(request, 'aula atualizada!')
        else:
            print(form_recurso.errors)
    return redirect('aula:buscar_aula', aula.slug)



def editar_recurso_aula(request, id, slug):
    aula = get_aula_by_slug(slug)
    recurso_antigo = get_recurso(id)
    form_recurso = RecursoForm(request.POST or None, instance = recurso_antigo)

    if form_recurso.is_valid():
        nome  = form_recurso.cleaned_data["nome"]
        descricao  = form_recurso.cleaned_data["descricao"]
        url  = form_recurso.cleaned_data["url"]
        arquivo  = form_recurso.cleaned_data["arquivo"]

        recurso_atualizado = Recurso(nome=nome, descricao=descricao, url=url, arquivo=arquivo)
        edit_recurso(recurso_antigo, recurso_atualizado)

        return redirect('aula:buscar_aula', aula.slug)


    context = { 'form_recurso': form_recurso, 'aula':aula }
    template_name = 'recursos/form.html'
    return render(request,template_name, context)



def remover_recurso_aula(request, slug, id):
    recurso = get_recurso(id)
    remove_recurso(recurso)

    return redirect('aula:buscar_aula', slug)
