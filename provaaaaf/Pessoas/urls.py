from django.urls import path

from .views import editar_Pessoas, list_Pessoas, criar_Pessoas, excluir_Pessoas


urlpatterns = [
    
    path('', list_Pessoas, nome='list_Pessoas'),
    path('novo', criar_Pessoas, nome='criar_pessoas'),
    path('editar/<int:id>/', editar_Pessoas, nome='editar_Pessoas'),
    path('deletar/int:id>/', excluir_Pessoas, nome ='excluir_Pessoas'),
]