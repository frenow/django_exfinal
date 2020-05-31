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
