import django_filters
from .models import Oportunidade

class OportunidadeFilter(django_filters.FilterSet):
    class Meta:
        model = Oportunidade
        fields = ['tipo']