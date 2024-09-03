from django.contrib import admin
from universidades.models import Universidade, Curso, AreaAtuacao, Cidade, Estado

# Classes de administração personalizadas (se necessário)
class UniversidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')
    list_filter = ('cidade',)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'universidade')
    search_fields = ('nome', 'universidade__nome')
    list_filter = ('universidade',)

class AreaAtuacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')
    search_fields = ('nome', 'estado__nome')
    list_filter = ('estado',)

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

# Registrando os modelos com as classes de administração
admin.site.register(Universidade, UniversidadeAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(AreaAtuacao, AreaAtuacaoAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Estado, EstadoAdmin)
