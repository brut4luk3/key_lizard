from django.shortcuts import render
from setores.models import Setor


# FUNC DO INDEX #
def index_setores(request):

    if request.user.is_authenticated:

        quantidade_setores = request.user.setor_set.all().count()

        if quantidade_setores == 0:

            sv = Setor(
                usuario=request.user,
                nome_setor='Vendas'
            )
            sv.save()

            sl = Setor(
                usuario=request.user,
                nome_setor='Locação'
            )
            sl.save()

            sa = Setor(
                usuario=request.user,
                nome_setor='Adminstrativo'
            )
            sa.save()

            return render(request, 'inicio_setores/index_setores.html')

        else:

            setores_listar = request.user.setor_set.all()

            context = {
                'setores_listar': setores_listar
            }

            return render(request, 'inicio_setores/index_setores.html', context=context)

    else:

        return render(request, 'inicio_setores/index_setores.html')
# FUNC DO INDEX - FIM #

# FUNC DO CADASTRO DE SETORES #
def registrar_setores(request):

    if request.method == 'GET':

        return render(request, 'cadastrar_setores/registrar_setores.html')

    elif request.method == 'POST':

        post_data = request.POST

        s = Setor(
            usuario=request.user,
            nome_setor=post_data.get('txtNomeSetor'),
        )

        s.save()

        return render(request, 'cadastrar_setores/sucesso_setores.html')
# FUNC DO CADASTRO DE SETORES - FIM #