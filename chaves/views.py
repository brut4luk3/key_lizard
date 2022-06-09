from django.shortcuts import render

def index_chaves(request):

    return render(request, 'inicio_chaves/index_chaves.html')
