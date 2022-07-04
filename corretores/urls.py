from django.urls import path

from . import views

app_name = 'corretores'

urlpatterns =[
    path('', views.index_corretores, name='index_corretores'),
    path('editar/<int:corretor_id>/', views.editar_corretores, name='editar_corretores'),
    path('excluir/', views.selecionar_excluir_corretores, name='selecionar_excluir_corretores'),
    path('excluir/<int:corretor_id>/', views.excluir_corretores, name='excluir_corretores'),
    path('cadastrar/', views.registrar_corretores, name='cadastrar_corretores')
]