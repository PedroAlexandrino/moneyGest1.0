from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
#Esta tabela serve para se quiseres guardar um historico do preço dos combustiveis
class TipoCombustivel(models.Model):
    tipo_combustivel = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=30,null=True)

    def __str__(self):
        return f"{self.tipo_combustivel} {self.descricao}"



class Carro(models.Model):
    modelo_carro = models.CharField(max_length=30)
    km_carro = models.IntegerField()
    tipo_combustivel = models.CharField(max_length=30)  

    def __str__(self):
        return f"{self.tipo_combustivel} {self.firstmodelo_carro_name} {self.km_carro}"



class Abastecimentos(models.Model):
    km_atuais_carro = models.IntegerField()
    litros = models.DecimalField(max_digits=10, decimal_places=2)
    preco_combustivel = models.DecimalField(max_digits=10, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.CharField(max_length=50, null=True)
    carro = models.ManyToManyField(Carro)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.carro} {self.km_atuais_carro} {self.preco_combustivel}$ {self.litros} {self.valor_pago}$ {self.data}"
