from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Carteira(models.Model):
    saldo = models.DecimalField(max_digits=10, decimal_places=2) #pode ser uma many to one para manteres um hstorico de saldo
    data = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) #Aqui poderá ser um many to many porque assim podes adicionar varias pessoas à mesma carteria
    

    def __str__(self):
        return f"{self.user} {self.saldo} {self.data}"

class Categoria(models.Model):
    categoria = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.categoria} {self.descricao}"

class Transacao_Carteira(models.Model):
    descricao = models.CharField(max_length=30,null=True)
    data = models.CharField(max_length=50, null=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    carteira = models.ManyToManyField(Carteira)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # PARA REVISÃO
    quantidade = models.IntegerField(null=True)
    carteira = models.ManyToManyField(Carteira,null=True)



    def __str__(self):
        return f"{self.data} {self.descricao} {self.carteira}$ {self.categoria} {self.valor_pago}"


