from django.shortcuts import render
from .models import Carro, Abastecimentos
from django.http import JsonResponse

from django.contrib.auth import get_user_model
User = get_user_model()


from datetime import datetime, timedelta


def carGest(request):
    print("entrou no carGest")
    usuario_atual = request.user
    print("User---> ", usuario_atual)
    #TENS DE VERIFICAR SE O USER JÁ TEM CARRO, SE NAO TIVER CARRO N PODE ADICIONAR ABASTECIMENTO
    return render(request, "home_car.html")

def addCarro(request):
    print("request-)", request.POST, request.user)
    user = User.objects.get(user=request.user)
    print("user_: ", user)
    Carro(modelo_carro = request.POST["modelo_carro"],
        km_carro = request.POST["km_carro"],
        tipo_combustivel = request.POST["tipo_combustivel"],
        user = request.user)
    """ Carro(modelo_carro= request.POST["modelo_carro"],
        km_carro = request.POST["km_carro"],tipo_combustivel = request.POST["tipo_combustivel"]).save() """


def delCarro(request):
    print("request", request.POST)
    carro = Carro.objects.get(id=request.POST["id"])    #TENS DE FORNECER O ID A PAGINA PARA DEPOIS VIR PELOS REQUESTS
    carro.delete()




def editCarro(request):
    print("request", request.POST)
    carro = Carro.objects.get(id=request.POST["id"]) 

    carro.modelo_carro = request.POST["modelo_carro"]
    carro.km_carro = request.POST["km_carro"]
    carro.tipo_combustivel = request.POST["tipo_combustivel"]


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
    #retorna json com todos os abastecimentos Default 3 meses anteriores ao dia atual mas tem de dar para (de x data a x data)
    """ CODIGO PARA DATAS """
    data_atual = datetime.now()
    data_tres_meses_atras = data_atual - timedelta(days=90)
    data_formatada = data_tres_meses_atras.strftime("%d/%m/%Y")
    print(data_formatada)
    """     FIM  """
    abastecimentos = Abastecimentos.objects.all()
    abastecimentos_array = []
    for i in abastecimentos:
        abastecimentos_array.append(i)
    
    #ver se este codigo retorna todos os abastecimentos
    ...
    
#func que vai devolver os gastos para uma determinada data/total(dsd sempre)
def gastosJson(request):
    gastos = Abastecimentos.objects.raw(""" SELECT * FROM carGest_abastecimentos, carGest_carro WHERE abastecimentos_id = carro_id """)
    #Devolve os gastos dos ultimos 3 meses (registos) + total gasto 
    #ver se dá para categorizar os gastos para teres um grafico redondo onde possas devolvar os gastos por categoria / dentro de um periodo de tempo
    
    """ CODIGO PARA DATAS """
    data_atual = datetime.now()
    data_tres_meses_atras = data_atual - timedelta(days=90)
    data_formatada = data_tres_meses_atras.strftime("%d/%m/%Y")
    print(data_formatada)
    """     FIM  """
    ...

#func vai devolver para os graficos a media de consumo para a data escolhida ou desde sempre
def mediaConsumo(request):
    #default são 3 meses, mas tem de dar para reutilizar esta func para dar para mais tempo
    #devolve media de consumo por 100km
    
    """ CODIGO PARA DATAS """
    data_atual = datetime.now()
    data_tres_meses_atras = data_atual - timedelta(days=90)
    data_formatada = data_tres_meses_atras.strftime("%d/%m/%Y")
    print(data_formatada)
    """     FIM  """

    ...


def previsoesAI(request):
    ...

