from django.views.generic import ListView
from .models import Oportunidade


class OportunidadeListView(ListView):
    """View para listar todas as oportunidades."""

    model = Oportunidade
    template_name = "oportunidades/oportunidades_lista.html"
    context_object_name = "oportunidades"
