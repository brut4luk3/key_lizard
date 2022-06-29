from django.shortcuts import render, get_object_or_404
from chaves.models import Chave
import datetime


# FUNC DO INDEX #
def index(request):

    return render(request, 'inicio/index.html')
# FUNC DO INDEX - FIM #

# FUNC DE SELEÇÃO #
def selecionar_chave(request):

    chaves_cadastradas = request.user.chave_set.all()

    context = {
        'chaves_cadastradas': chaves_cadastradas
    }

    return render(request, 'retirada/selecionar_chave.html', context=context)
# FUNC DE SELEÇÃO - FIM #

# FUNC DE RETIRADA #
def registrar_retirada(request, chave_id):

    if request.method == 'GET':

        chave = get_object_or_404(Chave, pk=chave_id)
        setores_cadastrados = request.user.setor_set.all()
        corretores_cadastrados = request.user.corretor_set.all()

        context = {
            'chave': chave,
            'setores_cadastrados': setores_cadastrados,
            'corretores_cadastrados': corretores_cadastrados
        }

        return render(request, 'retirada/registrar_retirada.html', context=context)

    elif request.method == 'POST':

        form_id_corretores = request.POST['menuCorretoresRetirada']
        horario_atualizado = datetime.datetime.now()

        chaves_retirada = Chave.objects.filter(pk=chave_id).update(corretor=form_id_corretores, horario=horario_atualizado)

        return render(request, 'retirada/sucesso_retirada.html')
# FUNC DE RETIRADA - FIM #