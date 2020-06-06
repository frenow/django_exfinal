from django.db import models
from django.apps import apps

class ReceberDAO(models.Manager):
    def novo(self, descricao, valor, data_venc, data_rec, situacao, c_id, f_id):
        
        if not data_rec:
            data_rec = None

        r = Receber(
        descricao = descricao, 
        valor = valor, 
        data_venc = data_venc, 
        data_rec = data_rec,
        situacao = situacao,
        classifica_id = c_id,
        forma_id = f_id)

        r.save()
        return r


    def editar(self, id, descricao, valor, data_venc, data_rec, situacao, c_id, f_id):
        r = Receber.objects.get(id=id)

        if not data_rec:
            data_rec = None

        r.descricao = descricao
        r.valor = valor
        r.data_venc = data_venc 
        r.data_pgto = data_rec
        r.situacao = situacao
        r.classifica_id = c_id
        r.forma_id = f_id
        
        r.save()
        return r
    
    def excluir(self, id):
        r = Receber.objects.get(id=id)

        r.delete()

    def rel(self, data_ini, data_fin):
        r = Receber.objects.filter(data_venc__range = [data_ini, data_fin])
        return r


class Receber(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(null=True, blank=True, default=None, max_digits=5, decimal_places=2)
    data_venc = models.DateTimeField(null=True)
    data_rec = models.DateTimeField(null=True)
    situacao = models.CharField(max_length=10)
    classifica = models.ForeignKey("Classifica_Receber", blank=True, null=True, on_delete=models.CASCADE)
    forma = models.ForeignKey("Forma_Receber", blank=True, null=True, on_delete=models.CASCADE)

    objects = ReceberDAO()

class Classifica_ReceberDAO(models.Manager):
    def novo(self, descricao):
        c = Classifica_Receber(descricao = descricao)

        c.save()
        return c


    def editar(self, id, descricao):
        c = Classifica_Receber.objects.get(id=id)

        c.descricao = descricao        
        c.save()
        return c

    def excluir(self, id):
        c = Classifica_Receber.objects.get(id=id)

        c.delete()

class Classifica_Receber(models.Model):
    
    descricao = models.CharField(max_length=200)

    objects = Classifica_ReceberDAO()

class Forma_ReceberDAO(models.Manager):
    def novo(self, descricao):
        f = Forma_Receber(descricao = descricao)

        f.save()
        return f


    def editar(self, id, descricao):
        f = Forma_Receber.objects.get(id=id)

        f.descricao = descricao        
        f.save()
        return f

    def excluir(self, id):
        f = Forma_Receber.objects.get(id=id)

        f.delete()

class Forma_Receber(models.Model):
    descricao = models.CharField(max_length=200)

    objects = Forma_ReceberDAO()