
from .models import Recurso


def get_recursos():
    return Recurso.objects.all()

def get_recurso(id):
    return Recurso.objects.get(id=id)

def add_recurso(recurso):
    return Recurso.objects.create(nome=recurso.nome, descricao=recurso.descricao, url=recurso.url, arquivo=recurso.arquivo)

def edit_recurso(recurso,edited):
    recurso.nome= edited.nome
    recurso.descricao= edited.descricao
    recurso.url= edited.url
    recurso.arquivo= edited.arquivo

    recurso.save(force_update=True)

def remove_recurso(recurso):
    recurso.delete()
