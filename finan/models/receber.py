from django.db import models
from django.apps import apps

class ReceberDAO(models.Manager):
    def novo(self, descricao, valor, data, data_rec, situacao):
        r = Receber(descricao = descricao, 
        valor = valor, 
        data = data, 
        data_rec = data_rec,
        situacao = situacao)

        r.save()
        return r


    def editar(self, id, descricao, valor, data, data_rec, situacao):
        r = Receber.objects.get(id=id)

        r.descricao = descricao, 
        r.valor = valor, 
        r.data = data, 
        r.data_rec = data_rec,
        r.situacao = situacao
        
        r.save()
        return r


class Receber(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(null=True, blank=True, default=None, max_digits=5, decimal_places=2)
    data = models.DateField(null=True)
    data_rec = models.DateField(null=True)
    situacao = models.CharField(max_length=10)

    objects = ReceberDAO()

class Classifica_Receber(models.Model):
    receber = models.ForeignKey("Receber", on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)

class Forma_Receber(models.Model):
    receber = models.ForeignKey("Receber", on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)