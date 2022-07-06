from django.urls import path

from . import views

app_name = 'setores'

urlpatterns =[
    path('', views.index_setores, name='index_setores'),
    path('editar/<int:setor_id>/', views.editar_setores, name='editar_setores'),
    path('excluir/', views.selecionar_excluir_setores, name='selecionar_excluir_setores'),
    path('excluir/<int:setor_id>/', views.excluir_setores, name='excluir_setores'),
    path('cadastrar/', views.registrar_setores, name='cadastrar_setores')
]