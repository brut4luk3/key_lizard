from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

def index_corretores(request):

    return render(request, 'inicio_corretores/index_corretores.html')
