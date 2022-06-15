from django.shortcuts import render
from corretores.models import Corretor
from setores.models import Setor
from chaves.models import Chave


# FUNC DO INDEX #
def index_chaves(request):

    return render(request, 'inicio_chaves/index_chaves.html')
# FUNC DO INDEX - FIM #

# FUNC DO CADASTRO DE CORRETORES #
def registrar_chaves(request):

    if request.method == 'GET':

        setores_cadastrados_chaves = request.user.setor_set.all()
        corretores_cadastrados_chaves = request.user.corretor_set.all()

        context = {
            'setores_cadastrados_chaves': setores_cadastrados_chaves,
            'corretores_cadastrados_chaves': corretores_cadastrados_chaves
        }

        return render(request, 'cadastrar_chaves/registrar_chaves.html', context=context)

    elif request.method == 'POST':

        post_data = request.POST
        form_id_setores = request.POST['menuSetoresChaves']
        form_id_corretores = request.POST['menuCorretoresChaves']

        setores = Setor.objects.get(pk=form_id_setores)
        corretores = Corretor.objects.get(pk=form_id_corretores)

        ch = Chave(
            usuario=request.user,
            corretor=corretores,
            setor_atribuido=setores,
            codigo=post_data.get('txtCodigoChave'),
            codigo_imovel_crm=post_data.get('txtCodigoCrm')
        )

        ch.save()

        return render(request, 'cadastrar_chaves/sucesso_chaves.html')
# FUNC DO CADASTRO DE CORRETORES - FIM #

# FUNC DO CADASTRO DE QUADRO #
def registrar_quadro(request):

    return render(request, 'cadastrar_chaves/registrar_quadro.html')
# FUNC DO CADASTRO DE QUADRO - FIM #
