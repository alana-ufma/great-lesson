from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('', listar_aulas, name='listar_aulas'),
    path('cadastrar', inserir_aula, name='inserir_aula'),
    # path('mostrar/<id>', buscar_aula, name='buscar_aula'),
    path('mostrar/<slug>', buscar_aula, name='buscar_aula'),
    path('visualizar/<slug>', preview_aula, name='preview_aula'),
    path('editar/<id>', editar_aula, name='editar_aula'),
    path('exemplo', exemplo_aula, name='exemplo_aula'),
    # path('remover/<id>', remover_aula, name='remover_aula'),

]
