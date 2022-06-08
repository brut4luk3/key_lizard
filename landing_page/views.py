from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

def landing_page(request):

    return HttpResponseRedirect(reverse('usuarios:index',))
