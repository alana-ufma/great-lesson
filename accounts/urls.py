from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('login/', login , name='login'),
    path('logout/', logout , name='logout'),
    path('dashboard/', dashboard , name='dashboard'),
    path('perfil/', profile , name='profile'),
    path('editar/', edit_profile , name='edit_profile'),
    path('trocarsenha/', edit_password , name='edit_password'),
    path('cadastrar/', register , name='register'),
    path('resetarsenha/', password_reset , name='password_reset'),
    path('confirmarsenha/<key>', password_reset_confirm , name='password_reset_confirm'),
    # path('cursos/', views.user_courses , name='user_courses'),


]
