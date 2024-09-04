from django.urls import path
from .views import ListaInteressesView, DetalheRespostasView

urlpatterns = [
    path('interesses/', ListaInteressesView.as_view(), name='lista_interesses'),
    path('interesses/<int:pk>/respostas/', DetalheRespostasView.as_view(), name='detalhe_respostas'),
]
