from django.db import models
from recurso.models import Recurso
from django.conf import settings
# from core.utils import unique_slug_generator

from recurso.models import Recurso

from ckeditor_uploader.fields import RichTextUploadingField


class Aula(models.Model):
    titulo =  models.CharField('Titulo', max_length=100, null=False, blank=False)
    slug =  models.CharField('Atalho', max_length=255, unique=True, blank=True, null=True)

    imagem =  models.ImageField('Foto', upload_to='media/images/aulas',  null=True, blank=True, max_length=500)
    descricao = RichTextUploadingField('Descricao', null=True,blank=True)
    leituras =  models.ManyToManyField(Recurso, blank=True, related_name="leituras")
    audios =  models.ManyToManyField(Recurso, blank=True, related_name="audios")
    demos =  models.ManyToManyField(Recurso, blank=True, related_name="demos")
    videos =  models.ManyToManyField(Recurso, blank=True, related_name="videos")
    discussoes =  models.ManyToManyField(Recurso, blank=True, related_name="discussoes")
    praticas =  models.ManyToManyField(Recurso, blank=True, related_name="praticas")
    ensinos =  models.ManyToManyField(Recurso, blank=True, related_name="ensinos")

    criador = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = 'criador', null=True, blank=True, related_name = 'aulas', on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField('Criado em', auto_now_add = True)
    updated_at = models.DateTimeField('Atualizado em', auto_now = True)

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['id']

    def __str__(self):
        return self.titulo

# def slug_save(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance, instance.titulo, instance.slug)
#
# pre_save.connect(slug_save, sender=Aula)
