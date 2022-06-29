from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from corretores.models import Corretor
from setores.models import Setor
from chaves.models import Chave
import string


# FUNC DO INDEX #
def index_chaves(request):

    if request.user.is_authenticated:

        chaves_listar = request.user.chave_set.all()

        context = {
            'chaves_listar': chaves_listar
        }

        return render(request, 'inicio_chaves/index_chaves.html', context=context)

    else:

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

    if request.method == 'GET':

        setores_cadastrados_chaves = request.user.setor_set.all()
        corretores_cadastrados_chaves = request.user.corretor_set.all()

        context = {
            'setores_cadastrados_chaves': setores_cadastrados_chaves,
            'corretores_cadastrados_chaves': corretores_cadastrados_chaves
        }

        return render(request, 'cadastrar_chaves/registrar_quadro.html', context=context)

    elif request.method == 'POST':

        form_id_setores = request.POST['menuSetoresChaves']
        form_id_corretores = request.POST['menuCorretoresChaves']

        setores_quadro = Setor.objects.get(pk=form_id_setores)
        corretores_quadro = Corretor.objects.get(pk=form_id_corretores)
        crm_quadro = Chave._meta.get_field('codigo_imovel_crm').get_default()

        alfabeto_string = string.ascii_uppercase
        alfabeto_lista = list(alfabeto_string)

        numeros_int = list(range(1, 20 + 1))
        numeros_lista = [str(x) for x in numeros_int]

        lista_letras = [list(x * 20) for x in alfabeto_lista]

        lista_numeros_gigante = list(numeros_lista * 26)

        lista_nova = [x for outra_lista in lista_letras for x in outra_lista]

        quadro_chaves = list(map(str.__add__, lista_nova, lista_numeros_gigante))

        for i in quadro_chaves:
            q = Chave(
                usuario=request.user,
                corretor=corretores_quadro,
                setor_atribuido=setores_quadro,
                codigo=i,
                codigo_imovel_crm=crm_quadro
            )

            q.save()

        return render(request, 'cadastrar_chaves/sucesso_quadro.html')
# FUNC DO CADASTRO DE QUADRO - FIM #

# FUNC DE EDIÇÃO DE CHAVES #
def editar_chaves(request, chave_id):

    if request.method == 'GET':

        chave = get_object_or_404(Chave, pk=chave_id)
        setores_cadastrados_editar = request.user.setor_set.all()
        corretores_cadastrados_editar = request.user.corretor_set.all()

        context = {
            'chave': chave,
            'setores_cadastrados_editar': setores_cadastrados_editar,
            'corretores_cadastrados_editar': corretores_cadastrados_editar
        }

        return render(request, 'editar_chaves/editar_chaves.html', context=context)

    elif request.method == 'POST':

        post_data_editar = request.POST

        form_id_setores = request.POST['menuSetoresEditar']
        form_id_corretores = request.POST['menuCorretoresEditar']
        form_imovel_crm = post_data_editar.get('txtCodigoCrmEditar')

        chaves_editadas = Chave.objects.filter(pk=chave_id).update(setor_atribuido=form_id_setores, corretor=form_id_corretores, codigo_imovel_crm=form_imovel_crm)

        return HttpResponseRedirect(reverse('chaves:index_chaves'),)
# FUNC DE EDIÇÃO DE CHAVES - FIM #

# FUNC DE SELEÇÃO #
def selecionar_excluir_chaves(request):

    chaves_cadastradas = request.user.chave_set.all()

    context = {
        'chaves_cadastradas': chaves_cadastradas
    }

    return render(request, 'excluir_chaves/selecionar_excluir_chaves.html', context=context)
# FUNC DE SELEÇÃO - FIM #

# FUNC DE EXCLUIR DE CHAVES #
def excluir_chaves(request, chave_id):
    if request.method == 'GET':

        chave = get_object_or_404(Chave, pk=chave_id)
        setores_cadastrados = request.user.setor_set.all()
        corretores_cadastrados = request.user.corretor_set.all()

        context = {
            'chave': chave,
            'setores_cadastrados': setores_cadastrados,
            'corretores_cadastrados': corretores_cadastrados
        }

        return render(request, 'excluir_chaves/excluir_chaves.html', context=context)

    elif request.method == 'POST':

        chave_excluida = Chave.objects.filter(id=chave_id).delete()

        return render(request, 'excluir_chaves/sucesso_excluir_chaves.html')
# FUNC DE EXCLUIR DE CHAVES - FIM #