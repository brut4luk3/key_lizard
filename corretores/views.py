from django.shortcuts import render

def index_corretores(request):

    return render(request, 'inicio_corretores/index_corretores.html')
