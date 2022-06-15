from django.urls import path

from . import views

app_name = 'chaves'

urlpatterns =[
    path('', views.index_chaves, name='index_chaves'),
    path('cadastrar/', views.registrar_chaves, name='cadastrar_chaves'),
    path('cadastrar/quadro/', views.registrar_quadro, name='cadastrar_quadro')
]