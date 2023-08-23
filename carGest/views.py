from django.shortcuts import render

# Create your views here.
def carGest(request):
    print("entrou no carGest")
    return render(request, "home_car.html")

def addCarro(request):
    ...
def delCarro(request):
    ...
def editCarro(request):
    ...

def addAbastecimento(request):
    ...
def editAbastecimento(request):
    ...

#func que vai devolver abastecimentos para uma determinada data, em formato json (p grafico)
def abastecimentosJson(request):
    ...
    
#func que vai devolver os gastos para uma determinada data/total(dsd sempre)
def gastosJson(request):
    ...

#func vai devolver para os graficos a media de consumo para a data escolhida ou desde sempre
def mediaConsumo(request):
    ...


def previsoesAI(request):
    ...

