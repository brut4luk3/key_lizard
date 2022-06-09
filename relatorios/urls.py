from django.urls import path

from . import views

app_name = 'relatorios'

urlpatterns =[
    path('', views.index_relatorios, name='index_relatorios')
]