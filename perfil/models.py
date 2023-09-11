from django.db import models

# Create your models here.


class Carteira(models.Model):
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.CharField(max_length=50, null=True)
    user = models.CharField(max_length=100,null=True)
    

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
    carteira = models.ManyToManyField(Carteira)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data} {self.descricao} {self.carteira}$ {self.categoria}"


