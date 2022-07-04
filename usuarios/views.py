from django.shortcuts import render, get_object_or_404
from setores.models import Setor
from corretores.models import Corretor
from chaves.models import Chave
import datetime


# FUNC DO INDEX #
def index(request):

    ultimas_chaves_retiradas = Chave.objects.all().order_by('-horario')[:10]

    context = {
        'ultimas_chaves_retiradas': ultimas_chaves_retiradas
    }

    return render(request, 'inicio/index.html', context=context)
# FUNC DO INDEX - FIM #

# FUNC DE SELEÇÃO #
def selecionar_chave(request):

    id_vendas = Setor.objects.get(nome_setor='Vendas')
    id_locacao = Setor.objects.get(nome_setor='Locação')

    chaves_cadastradas = request.user.chave_set.all()
    chaves_vendas = Chave.objects.filter(setor_atribuido=id_vendas).all()
    chaves_locacao = Chave.objects.filter(setor_atribuido=id_locacao).all()

    context = {
        'chaves_cadastradas': chaves_cadastradas,
        'chaves_vendas': chaves_vendas,
        'chaves_locacao': chaves_locacao
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

# FUNC DE SELEÇÃO - DEVOLUÇÃO #
def selecionar_chave_devolucao(request):

    id_vendas = Setor.objects.get(nome_setor='Vendas')
    id_locacao = Setor.objects.get(nome_setor='Locação')

    chaves_cadastradas = request.user.chave_set.all()
    chaves_vendas = Chave.objects.filter(setor_atribuido=id_vendas).all()
    chaves_locacao = Chave.objects.filter(setor_atribuido=id_locacao).all()

    context = {
        'chaves_cadastradas': chaves_cadastradas,
        'chaves_vendas': chaves_vendas,
        'chaves_locacao': chaves_locacao
    }

    return render(request, 'devolucao/selecionar_chave_devolucao.html', context=context)
# FUNC DE SELEÇÃO - DEVOLUÇÃO - FIM #

# FUNC DE DEVOLUÇÃO #
def registrar_devolucao(request, chave_id):

    if request.method == 'GET':

        chave = get_object_or_404(Chave, pk=chave_id)
        setores_cadastrados = request.user.setor_set.all()
        corretores_cadastrados = request.user.corretor_set.all()

        context = {
            'chave': chave,
            'setores_cadastrados': setores_cadastrados,
            'corretores_cadastrados': corretores_cadastrados
        }

        return render(request, 'devolucao/registrar_devolucao.html', context=context)

    elif request.method == 'POST':

        horario_atualizado = datetime.datetime.now()
        id_imobiliaria = Corretor.objects.get(nome='Imobiliária')

        chaves_devolvidas = Chave.objects.filter(pk=chave_id).update(corretor=id_imobiliaria, horario=horario_atualizado)

        return render(request, 'devolucao/sucesso_devolucao.html')
# FUNC DE DEVOLUÇÃO - FIM #