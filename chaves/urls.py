from django.urls import path

from . import views

app_name = 'chaves'

urlpatterns =[
    path('', views.index_chaves, name='index_chaves'),
    path('editar/<int:chave_id>/', views.editar_chaves, name='editar_chaves'),
    path('excluir/', views.selecionar_excluir_chaves, name='selecionar_excluir_chaves'),
    path('excluir/<int:chave_id>/', views.excluir_chaves, name='excluir_chaves'),
    path('cadastrar/', views.registrar_chaves, name='cadastrar_chaves'),
    path('cadastrar/quadro/', views.registrar_quadro, name='cadastrar_quadro')
]