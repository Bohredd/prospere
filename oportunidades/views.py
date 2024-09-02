from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from .models import Oportunidade
from .filterset import OportunidadeFilter

class OportunidadeListView(FilterView, ListView):
    model = Oportunidade
    template_name = 'oportunidades/lista.html'
    context_object_name = 'oportunidades'
    filterset_class = OportunidadeFilter

class OportunidadeDetailView(DetailView):
    model = Oportunidade
    template_name = 'oportunidades/detalhes.html'
    context_object_name = 'oportunidade'