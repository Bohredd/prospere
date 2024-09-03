# oportunidades/views.py

from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from .models import Oportunidade
from .filters import OportunidadeFilter  # Certifique-se de que o nome do arquivo é 'filters.py'

class OportunidadeListView(FilterView, ListView):
    model = Oportunidade
    template_name = 'oportunidades/lista.html'
    context_object_name = 'oportunidades'
    filterset_class = OportunidadeFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        # Adicione lógica adicional para o queryset, se necessário
        return queryset

class OportunidadeDetailView(DetailView):
    model = Oportunidade
    template_name = 'oportunidades/detalhes.html'
    context_object_name = 'oportunidade'
