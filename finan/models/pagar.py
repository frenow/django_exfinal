from django.db import models
from django.apps import apps

class PagarDAO(models.Manager):
    def novo(self, descricao, valor, data_venc, data_pgto, situacao, c_id, f_id):
        p = Pagar(descricao = descricao, 
        valor = valor, 
        data_venc = data_venc, 
        data_pgto = data_pgto,
        situacao = situacao,
        classifica_id = c_id,
        forma_id = f_id)

        p.save()
        return p


    def editar(self, id, descricao, valor, data_venc, data_pgto, situacao):
        p = Pagar.objects.get(id=id)

        p.descricao = descricao, 
        p.valor = valor, 
        p.data_venc = data_venc, 
        p.data_pgto = data_pgto,
        p.situacao = situacao
        
        p.save()
        return p

class Pagar(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.FloatField(null=True, blank=True, default=None)
    data_venc = models.DateField(null=True)
    data_pgto = models.DateField(null=True)
    situacao = models.CharField(max_length=10)
    classifica = models.ForeignKey("Classifica_Pagar", blank=True, null=True, on_delete=models.CASCADE)
    forma = models.ForeignKey("Forma_Pagar", blank=True, null=True, on_delete=models.CASCADE)

    objects = PagarDAO()

class Classifica_PagarDAO(models.Manager):
    def novo(self, descricao):
        c = Classifica_Pagar(descricao = descricao)

        c.save()
        return c


    def editar(self, id, descricao):
        c = Classifica_Pagar.objects.get(id=id)

        c.descricao = descricao        
        c.save()
        return c

    def excluir(self, id):
        c = Classifica_Pagar.objects.get(id=id)

        c.delete()

class Classifica_Pagar(models.Model):
    
    descricao = models.CharField(max_length=200)

    objects = Classifica_PagarDAO()

class Forma_PagarDAO(models.Manager):
    def novo(self, descricao):
        f = Forma_Pagar(descricao = descricao)

        f.save()
        return f


    def editar(self, id, descricao):
        f = Forma_Pagar.objects.get(id=id)

        f.descricao = descricao        
        f.save()
        return f

    def excluir(self, id):
        f = Forma_Pagar.objects.get(id=id)

        f.delete()

class Forma_Pagar(models.Model):
    descricao = models.CharField(max_length=200)

    objects = Forma_PagarDAO()