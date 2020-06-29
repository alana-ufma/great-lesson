
from .models import Aula


def get_aulas():
    return Aula.objects.all()

def get_aula(id):
    return Aula.objects.get(id=id)

def get_aula_by_slug(slug):
    return Aula.objects.get(slug=slug)


def add_aula(aula):
    return Aula.objects.create(titulo=aula.titulo, descricao=aula.descricao, leituras=aula.leituras, audios=aula.audios, demos=aula.demos, videos=aula.videos, ensinos=aula.ensinos, praticas=aula.praticas)

def edit_aula(aula,edited):
    aula.titulo= edited.titulo
    aula.descricao= edited.descricao
    aula.leituras= edited.leituras
    aula.audios= edited.audios
    aula.demos= edited.demos
    aula.videos= edited.videos
    aula.ensinos= edited.ensinos
    aula.praticas= edited.praticas

    aula.save(force_update=True)

def remove_aula(aula):
    aula.delete()
