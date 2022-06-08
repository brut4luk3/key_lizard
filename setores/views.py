from django.shortcuts import render

def index_setores(request):

    return render(request, 'inicio_setores/index_setores.html')
