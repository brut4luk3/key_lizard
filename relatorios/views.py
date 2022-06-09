from django.shortcuts import render

def index_relatorios(request):

    return render(request, 'inicio_relatorios/index_relatorios.html')
