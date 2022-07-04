from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
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

# FUNC DE EDIÇÃO DE CORRETORES #
def editar_corretores(request, corretor_id):

    if request.method == 'GET':

        corretor = get_object_or_404(Corretor, pk=corretor_id)
        setores_cadastrados_editar = request.user.setor_set.all()

        context = {
            'corretor': corretor,
            'setores_cadastrados_editar': setores_cadastrados_editar
        }

        return render(request, 'editar_corretores/editar_corretores.html', context=context)

    elif request.method == 'POST':

        post_data_editar = request.POST

        form_id_setores = request.POST['menuSetoresEditar']
        form_corretor_nome = post_data_editar.get('txtNomeCorretor')

        if form_corretor_nome == '':
            corretores_editados = Corretor.objects.filter(pk=corretor_id).update(setor=form_id_setores)

            return HttpResponseRedirect(reverse('corretores:index_corretores'),)
        else:
            corretores_editados = Corretor.objects.filter(pk=corretor_id).update(setor=form_id_setores, nome=form_corretor_nome)

            return HttpResponseRedirect(reverse('corretores:index_corretores'),)
# FUNC DE EDIÇÃO DE CORRETORES - FIM #

# FUNC DE SELEÇÃO #
def selecionar_excluir_corretores(request):

    corretores_cadastrados = request.user.corretor_set.all()

    context = {
        'corretores_cadastrados': corretores_cadastrados
    }

    return render(request, 'excluir_corretores/selecionar_excluir_corretores.html', context=context)
# FUNC DE SELEÇÃO - FIM #

# FUNC DE EXCLUIR DE CORRETORES #
def excluir_corretores(request, corretor_id):
    if request.method == 'GET':

        corretor = get_object_or_404(Corretor, pk=corretor_id)
        setores_cadastrados = request.user.setor_set.all()

        context = {
            'corretor': corretor,
            'setores_cadastrados': setores_cadastrados
        }

        return render(request, 'excluir_corretores/excluir_corretores.html', context=context)

    elif request.method == 'POST':

        corretor_excluido = Corretor.objects.filter(id=corretor_id).delete()

        return render(request, 'excluir_corretores/sucesso_excluir_corretores.html')
# FUNC DE EXCLUIR DE CORRETORES - FIM #
