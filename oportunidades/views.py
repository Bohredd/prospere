from django.views.generic import ListView, DetailView
from .models import Oportunidade


class OportunidadeListView(ListView):
    """View para listar todas as oportunidades."""

    model = Oportunidade
    template_name = "oportunidades/oportunidades_lista.html"
    context_object_name = "oportunidades"


class OportunidadeDetailView(DetailView):
    """View para detalhar a oportunidade."""
    model = Oportunidade
    template_name = 'oportunidades/oportunidade_detalhes.html'
    context_object_name = 'oportunidade'

    def get_object(self):
        return super().get_object()