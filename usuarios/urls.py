from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns =[
    path('', views.index, name='index'),
    path('retirada/', views.selecionar_chave, name='selecionar_chave'),
    path('retirada/<int:chave_id>/', views.registrar_retirada, name='registrar_retirada'),
    path('devolucao/', views.selecionar_chave_devolucao, name='selecionar_chave_devolucao'),
    path('devolucao/<int:chave_id>/', views.registrar_devolucao, name='registrar_devolucao')
]

