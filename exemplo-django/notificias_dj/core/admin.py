from django.contrib import admin

from .models import Categoria, Noticia

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia)