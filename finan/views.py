from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from .models import Pagar, Receber, Forma_Pagar, Forma_Receber, Classifica_Receber, Classifica_Pagar

def index(request):
    return render(request, 'index.html')

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar_class_pagar(request):
    result = Classifica_Pagar.objects.all()
    template = loader.get_template('listar_class_pagar.html')
    context = {
        'lista' : result,
    }
    return HttpResponse(template.render(context, request))

def cadastro_class_pagar(request):
    return render(request, 'cadastro_class_pagar.html')

def cadastrar_class_pagar(request):
    c = Classifica_Pagar.objects.novo(request.POST['descricao'])
    return HttpResponse(f"{c.descricao} cadastrado com sucesso")

def detalhar_class_pagar(request, id_class):
    c = Classifica_Pagar.objects.get(id=id_class)
    context = {'class':c}
    return render(request, 'detalhe_class_pagar.html', context)

def editar_class_pagar(request, id_class):
    c = Classifica_Pagar.objects.get(id=id_class)
    context = {'class':c}
    return render(request, 'editar_class_pagar.html', context)

def edit_class_pagar(request):
    c = Classifica_Pagar.objects.editar(request.POST['id'], request.POST['descricao'])
    return HttpResponse(f"{c.descricao} alterado com sucesso")

def excluir_class_pagar(request, id_class):
    Classifica_Pagar.objects.excluir(id_class)
    return HttpResponse(f"{id_class} excluido com sucesso")

def listar_forma_pagar(request):
    result = Forma_Pagar.objects.all()
    template = loader.get_template('listar_forma_pagar.html')
    context = {
        'lista' : result,
    }
    return HttpResponse(template.render(context, request))

def cadastro_forma_pagar(request):
    return render(request, 'cadastro_forma_pagar.html')

def cadastrar_forma_pagar(request):
    f = Forma_Pagar.objects.novo(request.POST['descricao'])
    return HttpResponse(f"{f.descricao} cadastrado com sucesso")

def detalhar_forma_pagar(request, id_forma):
    f = Forma_Pagar.objects.get(id=id_forma)
    context = {'forma':f}
    return render(request, 'detalhe_forma_pagar.html', context)

def editar_forma_pagar(request, id_forma):
    f = Forma_Pagar.objects.get(id=id_forma)
    context = {'forma':f}
    return render(request, 'editar_forma_pagar.html', context)

def edit_forma_pagar(request):
    f = Forma_Pagar.objects.editar(request.POST['id'], request.POST['descricao'])
    return HttpResponse(f"{f.descricao} alterado com sucesso")

def excluir_forma_pagar(request, id_forma):
    Forma_Pagar.objects.excluir(id_forma)
    return HttpResponse(f"{id_forma} excluido com sucesso")

def listar_pagar(request):
    result = Pagar.objects.all()
    template = loader.get_template('listar_pagar.html')
    context = {
        'lista' : result,
    }
    return HttpResponse(template.render(context, request))

def cadastro_pagar(request):
    situacao = ['ABERTO','BAIXADO']
    forma = Forma_Pagar.objects.all()
    classifica = Classifica_Pagar.objects.all()
    template = loader.get_template('cadastro_pagar.html')
    context = {
        'forma': forma,
        'classifica': classifica,
        'situacao': situacao,
    }
    return HttpResponse(template.render(context, request))

def cadastrar_pagar(request):
    p = Pagar.objects.novo(request.POST['descricao'], request.POST['valor'], request.POST['data_venc'], request.POST['data_pgto'], request.POST['situacao'], request.POST['c_id'], request.POST['f_id'])
    return HttpResponse(f"{p.descricao} cadastrado com sucesso")

def detalhar_pagar(request, id_pagar):
    p = Pagar.objects.get(id=id_pagar)
    context = {'pagar':p}
    return render(request, 'detalhe_pagar.html', context)

def editar_pagar(request, id_pagar):
    p = Pagar.objects.get(id=id_pagar)
    forma = Forma_Pagar.objects.all()
    classifica = Classifica_Pagar.objects.all()
    situacao = ['ABERTO','BAIXADO']
    context = {
        'pagar':p,
        'situacao':situacao,
        'forma': forma,
        'classifica': classifica,
    }
    return render(request, 'editar_pagar.html', context)

def edit_pagar(request):
    p = Pagar.objects.editar(request.POST['id'], request.POST['descricao'], request.POST['valor'], request.POST['data_venc'], request.POST['data_pgto'], request.POST['situacao'], request.POST['c_id'], request.POST['f_id'])
    return HttpResponse(f"{p.descricao} alterado com sucesso")

def excluir_pagar(request, id_pagar):
    Pagar.objects.excluir(id_pagar)
    return HttpResponse(f"{id_pagar} excluido com sucesso")
