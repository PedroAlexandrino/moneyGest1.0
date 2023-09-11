from django.shortcuts import render
from .models import Carro, Abastecimentos
from django.http import JsonResponse


# Create your views here.
def carGest(request):
    print("entrou no carGest")
    #TENS DE VERIFICAR SE O USER JÁ TEM CARRO, SE NAO TIVER CARRO N PODE ADICIONAR ABASTECIMENTO
    return render(request, "home_car.html")

def addCarro(request):
    print("request-)", request.POST)
    """ Carro(modelo_carro= request.POST["modelo_carro"],
        km_carro = request.POST["km_carro"],tipo_combustivel = request.POST["tipo_combustivel"]).save() """
    ...
def delCarro(request):
    ...
def editCarro(request):
    ...
def getCarro(request=None):
    carros_bd = Carro.objects.all()
    carros = []
    for i in carros_bd:
        carros.append(i.modelo_carro)
    print("Array carros... ", carros)
    return JsonResponse({"carros":carros, "message":"OK"})

def addAbastecimento(request):
    print("request-)", request.POST)
    """ carro = Carro.objects.get(id= request.POST["id_carro"])
    Abastecimentos(km_atuais_carro = request.POST["km_atuais_carro"],
        litros = request.POST["litros"],
        preco_combustivel = request.POST["preco_combustivel"],
        valor_pago = request.POST["valor_pago"],
        data = request.POST["data"],
        carro = carro).save() """
    

    ...
def editAbastecimento(request):
    ...

#func que vai devolver abastecimentos para uma determinada data, em formato json (p grafico)
def abastecimentosJson(request):
    ...
    
#func que vai devolver os gastos para uma determinada data/total(dsd sempre)
def gastosJson(request):
    gastos = Abastecimentos.objects.raw(""" SELECT * FROM carGest_abastecimentos, carGest_carro WHERE abastecimentos_id = carro_id """)
    ...

#func vai devolver para os graficos a media de consumo para a data escolhida ou desde sempre
def mediaConsumo(request):
    ...


def previsoesAI(request):
    ...

