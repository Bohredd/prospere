from django.views.generic import ListView, DetailView
from .models import Evento


class EventosListView(ListView):
    """View para listar todas as oportunidades."""

    model = Evento
    template_name = "eventos/eventos_lista.html"
    context_object_name = "eventos"


class EventoDetailView(DetailView):
    """View para detalhar a oportunidade."""
    model = Evento
    template_name = 'eventos/evento_detalhes.html'
    context_object_name = 'evento'

    def get_object(self):
        return super().get_object()