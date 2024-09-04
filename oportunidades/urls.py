from django.urls import path
from .views import OportunidadeListView, OportunidadeDetailView, InteresseFormView

urlpatterns = [
    path('', OportunidadeListView.as_view(), name='listar_oportunidades'),
    path('<int:pk>/', OportunidadeDetailView.as_view(), name='detalhes_oportunidade'),
    path("<int:pk>/interesse/", InteresseFormView.as_view(), name="interesse_oportunidade"),
]