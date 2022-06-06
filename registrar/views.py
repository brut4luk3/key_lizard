from django.shortcuts import render

from django.contrib.auth.models import User
from usuarios.models import Profile


def novo(request):

    if request.method == 'GET':

        return render(request, 'registrar/novo.html')

    elif request.method == 'POST':

        post_data = request.POST

        u = User(
            username=post_data.get('txtUsername'),
            email=post_data.get('txtEmail'),
            first_name=post_data.get('txtFirstName'),
            last_name=post_data.get('txtLastName')
        )

        return render(request, 'registrar/sucesso.html')