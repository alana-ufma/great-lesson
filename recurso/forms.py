
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Recurso

class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['nome', 'descricao', 'url', 'arquivo']
        labels = {
            'nome':_('Nome'),
            'descricao':_('Descrição'),
            'url':_('Link'),
            'arquivo':_('Arquivo'),}
