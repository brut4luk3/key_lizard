from django.shortcuts import render
from corretores.models import Corretor
from setores.models import Setor


# FUNC DO INDEX #
def index_corretores(request):

    if request.user.is_authenticated:

        corretores_listar = request.user.corretor_set.all()

        context = {
            'corretores_listar': corretores_listar
        }

        return render(request, 'inicio_corretores/index_corretores.html', context=context)

    else:

        return render(request, 'inicio_corretores/index_corretores.html')
# FUNC DO INDEX - FIM #

# FUNC DO CADASTRO DE CORRETORES #
def registrar_corretores(request):

    if request.method == 'GET':

        setores_cadastrados = request.user.setor_set.all()

        context = {
            'setores_cadastrados': setores_cadastrados
        }

        return render(request, 'cadastrar_corretores/registrar_corretores.html', context=context)

    elif request.method == 'POST':

        post_data = request.POST
        form_id_setores = request.POST['menuSetores']

        setores = Setor.objects.get(pk=form_id_setores)

        c = Corretor(
            usuario=request.user,
            setor=setores,
            nome=post_data.get('txtNomeCorretor')
        )

        c.save()

        return render(request, 'cadastrar_corretores/sucesso_corretores.html')
# FUNC DO CADASTRO DE CORRETORES - FIM #
