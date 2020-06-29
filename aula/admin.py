from django.contrib import admin

# Register your models here.
from .models import Aula

class AulaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titulo",)}


admin.site.register(Aula, AulaAdmin)
