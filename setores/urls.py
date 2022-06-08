from django.urls import path

from . import views

app_name = 'setores'

urlpatterns =[
    path('', views.index_setores, name='index_setores')
]