from django.shortcuts import render
from .models import Carro, Abastecimentos
from django.http import JsonResponse

from django.contrib.auth import get_user_model
User = get_user_model()


from datetime import datetime, timedelta
from django.utils import timezone



"""                     Inicio de codigo para carro                 """

def carGest(request):
    print("entrou no carGest")
    usuario_atual = request.user
    #TENS DE VERIFICAR SE O USER JÁ TEM CARRO, SE NAO TIVER CARRO N PODE ADICIONAR ABASTECIMENTO
    # aqui tenho de mandar todos os dados para este certo utilizador
    print("User:", request.user)

    user = User.objects.get(username=request.user)
    carros = Carro.objects.filter(user=user)
    
    #   TENS DE ADAPTAR ESTES ABASTECIMENTOS PARA SEREM SÓ DO CARRO DO UTILIZADOR
    #abastecimentos = Abastecimentos.objects.filter(carro__in = carros)

    #abastecimentos = Abastecimentos.carro.through.objects.filter(carro_id=carros.values().get("id"))
    
    abastecimentos = Abastecimentos.objects.filter(carro__in=carros)
    abastecimentos_array = []
    print("len i->",len(abastecimentos),len(carros))
    for i in abastecimentos.values():
        print("i->",i)
        abastecimentos_array.append(i)

    carros = Carro.objects.filter(user=request.user)
    abastecimentos = Abastecimentos.objects.filter(carro__in=carros)
    print("carros",carros, "  Abastecimentos:  ", abastecimentos)

    return render(request, "home_car.html",{"user": request.user})


def addCarro(request):
    print("request-)", request.POST)

    user = User.objects.get(username=request.user)
    print("user_: ", user)
    Carro(modelo_carro = request.POST["marca_modelo"],
        km_carro = request.POST["km_carro"],
        tipo_combustivel = request.POST["tipo_combustivel"],
        user = user).save()
    """ Carro(modelo_carro= request.POST["modelo_carro"],
        km_carro = request.POST["km_carro"],tipo_combustivel = request.POST["tipo_combustivel"]).save() """
    return JsonResponse({"message":"OK"})


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
    carro.save()


def getCarro(request=None):
    carros_bd = Carro.objects.filter(user=request.user)
    carros = []
    carros_id = []
    for i in carros_bd:
        carros.append(i.modelo_carro)
        carros_id.append(i.id)
    print("Array carros... ", carros_id)
    return JsonResponse({"carros":carros, "carros_id":carros_id,"message":"OK"})

"""                     Fim de codigo para carro                 """



"""                     Inicio de codigo para Abastecimentos                 """

def addAbastecimento(request):
    data_atual = datetime.now()
    data_tres_meses_atras = data_atual
    data_formatada = data_tres_meses_atras.strftime("%Y-%m-%d %H:%M:%S")
    data_string = data_formatada
    data_inicial = datetime.strptime(data_string, "%Y-%m-%d %H:%M:%S")
    data_inicial = timezone.make_aware(data_inicial, timezone.utc)

    print("addAbastecimento request-)", request.POST)
    carro = Carro.objects.get(id = request.POST["id_carro"]).__getattribute__("id")
    abastecimento = Abastecimentos.objects.create(
            km_atuais_carro=request.POST["km_atuais_carro"],
            litros=request.POST["litros"],
            preco_combustivel=request.POST["preco_combustivel"],
            valor_pago=request.POST["valor_pago"],
            data=data_inicial
        )
    # Adiciona o relacionamento ManyToMany
    abastecimento.carro.add(carro)
        
    abastecimento_novo = []
    for i in abastecimento.__dict__:
        abastecimento_novo.append(i)
    abastecimento.save()
    

    return JsonResponse({"message":"OK","abastecimento":abastecimento_novo}) 

def editAbastecimento(request):
    print("request-)", request.POST)
    carro = Carro.objects.get(id= request.POST["id_carro"])
    
    abastecimento = Abastecimentos.objects.get(id = request.POST["id_abastecimento"])

    abastecimento.km_atuais_carro = request.POST["km_atuais_carro"]
    abastecimento.litros = request.POST["litros"]
    abastecimento.preco_combustivel = request.POST["preco_combustivel"]
    abastecimento.valor_pago = request.POST["valor_pago"]
    abastecimento.data = request.POST["data"]
    abastecimento.carro = carro
    #abastecimento.save()
    return JsonResponse({"message":"OK","abastecimento":abastecimento})   


def deleteAbastecimento(request):
    print("del --", request.POST)
    abastecimento = Abastecimentos.objects.get(id = request.POST["id_abastecimento"]).delete()
    return JsonResponse({"message":"OK","abastecimento":abastecimento})   


#func que vai devolver abastecimentos para uma determinada data, em formato json (p grafico)
def abastecimentosJson(request):
    print("entrou no abastecimentosJson",request.POST)
    #retorna json com todos os abastecimentos Default 3 meses anteriores ao dia atual mas tem de dar para (de x data a x data)
    if int(request.POST["opcao"]) == 0:
        user = User.objects.get(username=request.user)
        carros = Carro.objects.filter(user=user)
        """ CODIGO PARA DATAS """
        data_atual = datetime.now()
        data_tres_meses_atras = data_atual - timedelta(days=90)
        data_formatada = data_tres_meses_atras.strftime("%d/%m/%Y %H:%S")
        print("abastecimentosJson data pcao 0---> ",data_formatada)
        """     FIM  """
        abastecimentos = Abastecimentos.objects.filter(carro__in=carros)
        abastecimentos_array = []
        print("len i->",len(abastecimentos),len(carros))
        km_antigos=0
        km_andados={}
        for i in abastecimentos.values():
            km_andados = i.get("km_atuais_carro") - km_antigos #falta passar esta conta para o json 
            km_antigos = i.get("km_atuais_carro")
            print("i->",km_andados)
            abastecimentos_array.append(i)
            abastecimentos_array.append(km_andados)
        return JsonResponse({"message":"OK","abastecimentos":abastecimentos_array})   

    elif int(request.POST["opcao"]) == 1:
        #queres por os dados no grafico default (ultimos 6 meses) media por 100km
        """ CODIGO PARA DATAS """
        data_atual = datetime.now()
        data_tres_meses_atras = data_atual - timedelta(weeks=26)
        data_formatada = data_tres_meses_atras.strftime("%Y-%m-%d %H:%M:%S")

        data_string = data_formatada
        data_inicial = datetime.strptime(data_string, "%Y-%m-%d %H:%M:%S")
        data_inicial = timezone.make_aware(data_inicial, timezone.utc)
        print("abastecimentosJson data pcao 1---> ",data_inicial)
        """     FIM  """
        user = User.objects.get(username=request.user)
        carros = Carro.objects.filter(user=user)
      
        print("abastecimentos len(",len(Abastecimentos.objects.filter(carro__in=carros,data__gte=data_inicial)),") ->",data_formatada)
        abastecimentos_array = []
        data_antiga_bd = Abastecimentos.objects.filter(carro__in=carros).filter(data__gte=data_formatada).order_by('data')
        mes_anterior = None
        litros_antigo=0
        km_antigo = 0
        itera = 0
        mes_atual = ""
        media = {}
        media_final = {}
        for i in data_antiga_bd:
            #print("i->",i)
            #date_obj = datetime.strptime(stri.data, "%Y-%m-%d %H:%M:%S")
            mes_atual = i.data.month #
            mes_atual = i.data.strftime("%B")
            print("mes_atual-> ",mes_atual)
            if mes_anterior is None or not mes_anterior in media:
                mes_anterior = mes_atual
                #print("mes_anterior None-> ",mes_anterior,"conta_->",i.km_atuais_carro / i.litros * 100)
                media[mes_anterior] = (i.litros  / i.km_atuais_carro)* 100
                print("conta: ", i.km_atuais_carro , i.litros, (i.km_atuais_carro / i.litros ))
                litros_antigo = i.litros  
                itera += 1
            elif mes_atual == mes_anterior:
                #print(f"O mes_anterior é igual {mes_anterior} para mes_atual: {mes_atual}  Na data {i.data}")
                media[mes_anterior] += (litros_antigo / (i.km_atuais_carro - km_antigo)) * 100
                litros_antigo = i.litros    
                itera += 1
                #print("media",media, ((i.km_atuais_carro - km_antigo) / litros_antigo) * 100)

            


            elif mes_atual != mes_anterior:
                #print(f"O mes_anterior MUDOU {mes_anterior} para mes_atual: {mes_atual}  Na data {i.data}")
                print("itera",itera)
                #litros_antigo = i.litros
                #itera += 1
                #print("media_final[mes_anterior] = media[mes_anterior] / itera",media[mes_anterior], mes_anterior, itera)
                media_final[mes_anterior] = media[mes_anterior] / itera
                mes_anterior = mes_atual
                
                itera = 0
        if mes_anterior is not None:
            media_final[mes_anterior] = media[mes_anterior] / itera
        print("media_final--->",media_final,media)
            #se o mês não mudou, soma valor à media e quando o mês mudar somas todos os valores ao array das medias e divides pela quantidade de valores
            # a conta anteriror é ( media[mes_anterior] += i.km_atuais_carro - km_antigo / litros_antigo * 100 )
            #   pois queres andar sempre a saber qual é a media entre abastecimentos e ires adicionando essa media ao array
            # depois queres montar um dict com "mes" : media para passar para a view 

        data_atual = datetime.now()
        nomes_meses = []
        for _ in range(6):
            data_atual -= timedelta(days=30)  # Subtrai aproximadamente 30 dias (1 mês)
            nome_mes = data_atual.strftime('%B')  # Obtém o nome do mês
            nomes_meses.append(nome_mes)
        nomes_meses.reverse()
        print("nomes_meses",nomes_meses)
        return JsonResponse({"message":"OK","media":media_final, "meses":nomes_meses})   
        
    elif int(request.POST["opcao"]) == 2:
        user = User.objects.get(username=request.user)
        carros = Carro.objects.filter(user=user)
        id_carros = []
        for i in carros:
            id_carros.append(i.id)
        """ CODIGO PARA DATAS """
        data_atual = datetime.now()
        data_tres_meses_atras = data_atual - timedelta(days=90)
        data_formatada = data_tres_meses_atras.strftime("%d/%m/%Y %H:%S")
        print("abastecimentosJson data pcao 0---> ",data_formatada)
        """     FIM  """
        #   TENS DE ADAPTAR ESTES ABASTECIMENTOS PARA SEREM SÓ DO CARRO DO UTILIZADOR
        #abastecimentos = Abastecimentos.objects.filter(carro__in = carros)

        #abastecimentos = Abastecimentos.carro.through.objects.filter(carro_id=carros.values().get("id"))
        
        abastecimentos = Abastecimentos.objects.filter(carro__in=carros)
        abastecimentos_array = []
        print("len i->",len(abastecimentos),len(carros))
        for i in abastecimentos.values():
            #print("i->",i)
            abastecimentos_array.append(i)
        # Defina as duas datas que você deseja comparar
        data1 = datetime(2023, 6, 15)  # Substitua com sua primeira data (data de hoje)
        print("id_carros-> ",id_carros)
        data_antiga_bd = Abastecimentos.objects.raw(""" SELECT MIN(data) from carGest_abastecimentos UNION  SELECT * from carGest_abastecimentos_carro WHERE carro_id = {carros} """)
        #aqui queres ir buscar a data mais antiga para veres os meses de difrença para mandares para dps converter nos nomes dos meses
        data2 = datetime(2022, 11, 20)  # Substitua com sua segunda data (data_antiga_bd)

        # Calcule a diferença entre as datas
        diferenca = abs((data1.year - data2.year) * 12 + data1.month - data2.month)

        # Imprima a diferença de meses
        print(f'A diferença de meses entre as datas é: {diferenca} meses')
        km_antigo = 0
        litros_antigo = 0
        soma=0
        mes_atual = ""
        mes_anterior = None
        media = {}
        media_final = {}
        itera = 0
        for i in abastecimentos:
            date_obj = datetime.strptime(i.data, "%d/%m/%Y %H:%M")
            mes_atual = date_obj.month # ver se no array apenas fica guardfado o mês, ou se tambem fica o ano, em principio fica só o mes
            if mes_anterior is None:
                #codigo para verificar se os abastecimentos mudaram de mês
                # se o mês não mudar podes ir continuando a somar os litros e os km andados
                # se mudar fazes um dict {mes: media}
                mes_anterior = mes_atual
                itera += 1
            elif mes_atual == mes_anterior:
                print(f"O mês é igual {mes_anterior} para {mes_atual} na data {i.data}")
                media[mes_anterior] += i.km_atuais_carro - km_antigo / litros_antigo * 100
                litros_antigo = i.litros    
                itera += 1
            


            elif mes_atual != mes_anterior:
                print(f"O mês mudou de {mes_anterior} para {mes_atual} na data {i.data}")
                mes_anterior = mes_atual
                litros_antigo = i.litros
                media_final[mes_anterior] = media[mes_anterior] / itera

            soma = i.km_atuais_carro - km_antigo
            litros = litros_antigo
            km_antigo = i.km_atuais_carro 
            print("Soma-->",soma)
 


        
        #NO ARRAY abastecimentos_array deves ter todos os abastecimentos
        # tens de ter um dict onde tenhas o mes : media (ou outra metrica)
        #para calculares a media tens de ir buscar os km da linha atual comparares com os da linha seguinte e veres quantos litros puseste
        # e fazes essa conta vezes 100KM 




        return JsonResponse({"message":"OK","abastecimentos":abastecimentos_array})   


"""                     Fim de codigo para Abastecimentos                 """


    
#func que vai devolver os gastos para uma determinada data/total(dsd sempre)
def gastosJson(request):
    valor_pago_total=0      #var que vai guardar o valor total gasto nos abastecimentos
    #agora tem de devolver por mês para dar os tais graficos
    user = User.objects.get(username=request.user)
    carros = Carro.objects.filter(user=user)
    """ CODIGO PARA DATAS """
    data_atual = datetime.now()
    data_tres_meses_atras = data_atual - timedelta(days=90)
    data_formatada = data_tres_meses_atras.strftime("%d/%m/%Y %H:%S")
    print("abastecimentosJson data pcao 0---> ",data_formatada)
    """     FIM  """
    abastecimentos = Abastecimentos.objects.filter(carro__in=carros)
    for i in abastecimentos:
        valor_pago_total += i.valor_pago
    
#func vai devolver para os graficos a media de consumo para a data escolhida ou desde sempre
def mediaConsumo(request):
    #default são 3 meses, mas tem de dar para reutilizar esta func para dar para mais tempo
    #devolve media de consumo por 100km
    #também pode devolver um array com todas as medias por mês para o user ver como lista
    
    
    """ CODIGO PARA DATAS """
    data_atual = datetime.now()
    data_tres_meses_atras = data_atual - timedelta(days=90)
    data_formatada = data_tres_meses_atras.strftime("%d/%m/%Y")
    print(data_formatada)
    """     FIM  """

    ...


def previsoesAI(request):
    ...

