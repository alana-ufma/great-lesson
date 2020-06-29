
from django import forms
from django.utils.translation import gettext_lazy as _
from aula.models import Aula

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['titulo', 'descricao', 'imagem']
        labels = {
            'titulo':_('Título'),
            'descricao':_('Descrição'),
    
        }
