from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', listar, name='listar'),
    path('salvar/<id>', salvar_recurso_aula, name='salvar_recurso_aula'),
    # path('cadastrar', inserir_aula, name='inserir_aula'),
    # path('mostrar/<id>', buscar_aula, name='buscar_aula'),
    path('<slug>/editar/<id>', editar_recurso_aula, name='editar_recurso_aula'),
    path('<slug>/deletar/<id>', remover_recurso_aula, name='remover_recurso_aula'),

    # path('remover/<id>', remover_aula, name='remover_aula'),

]
