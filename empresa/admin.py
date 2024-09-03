from django.contrib import admin
from empresa.models import Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'endereco', 'telefone', 'email', 'site')
    search_fields = ('nome', 'cnpj', 'email')
