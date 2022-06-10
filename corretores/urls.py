from django.urls import path

from . import views

app_name = 'corretores'

urlpatterns =[
    path('', views.index_corretores, name='index_corretores'),
    path('cadastrar/', views.registrar_corretores, name='cadastrar_corretores')
]