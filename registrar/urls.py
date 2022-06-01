from django.urls import path

from . import views


app_name = 'registrar'

urlpatterns = [
    path('novo/', views.novo, name='novo')
]