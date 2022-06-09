from django.urls import path

from . import views

app_name = 'chaves'

urlpatterns =[
    path('', views.index_chaves, name='index_chaves')
]