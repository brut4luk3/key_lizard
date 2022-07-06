from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
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

# FUNC DE EDIÇÃO DE SETORES #
def editar_setores(request, setor_id):

    if request.method == 'GET':

        setor = get_object_or_404(Setor, pk=setor_id)
        setores_cadastrados_editar = request.user.setor_set.all()

        context = {
            'setor': setor,
            'setores_cadastrados_editar': setores_cadastrados_editar
        }

        return render(request, 'editar_setores/editar_setores.html', context=context)

    elif request.method == 'POST':

        post_data_editar = request.POST
        form_setor_nome = post_data_editar.get('txtNomeSetor')

        setores_editados = Setor.objects.filter(pk=setor_id).update(nome_setor=form_setor_nome)

        return HttpResponseRedirect(reverse('setores:index_setores'),)
# FUNC DE EDIÇÃO DE SETORES - FIM #

# FUNC DE SELEÇÃO #
def selecionar_excluir_setores(request):

    setores_cadastrados = request.user.setor_set.all()

    context = {
        'setores_cadastrados': setores_cadastrados
    }

    return render(request, 'excluir_setores/selecionar_excluir_setores.html', context=context)
# FUNC DE SELEÇÃO - FIM #

# FUNC DE EXCLUIR DE SETORES #
def excluir_setores(request, setor_id):
    if request.method == 'GET':

        setor = get_object_or_404(Setor, pk=setor_id)
        setores_cadastrados = request.user.setor_set.all()

        context = {
            'setor': setor,
            'setores_cadastrados': setores_cadastrados
        }

        return render(request, 'excluir_setores/excluir_setores.html', context=context)

    elif request.method == 'POST':

        setor_excluido = Setor.objects.filter(id=setor_id).delete()

        return render(request, 'excluir_setores/sucesso_excluir_setores.html')
# FUNC DE EXCLUIR DE SETORES - FIM #