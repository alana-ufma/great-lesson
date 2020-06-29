from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

class Recurso(models.Model):
    nome =  models.CharField('Nome', max_length=100, null=False, blank=False)
    descricao = RichTextUploadingField('Descricao', null=True,blank=True)

    url =  models.URLField('Url', null=True, blank=True)
    arquivo =  models.FileField('Arquivo', null=True, blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add = True)
    updated_at = models.DateTimeField('Atualizado em', auto_now = True)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
        ordering = ['id']

    def __str__(self):
        return self.nome
