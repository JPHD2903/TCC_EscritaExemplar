from django.contrib import admin
from .models import Usuario, Redacao

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "nickname", "email", "senha")

@admin.register(Redacao)
class RedacaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "texto", 'modalidade', 'data_publicacao')
