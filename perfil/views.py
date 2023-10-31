from django.shortcuts import render, redirect
from perfil.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from .models import Carteira, Categoria, Transacao_Carteira
User = get_user_model()

def main(request):
    print("request.user---",request.user)
    user = request.user
    print("entrou no main")
    return render(request, "home.html",{"user": user})

def pagina_login(request):
    logout(request)
    print("Utilizador foi deslogado")
    return render(request, "login.html")

def do_login(request):
    if request.method == "POST":
        #logout_view(request.user)
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        print("request.user---",request.POST,user,user is not None)
        if user is not None:
            print("Utilizador foi encontrado",user)
            login(request, user)
            print("Utilizador foi logado",login)
            return render(request, "home.html",{"user": user})
        else:
            print("Utilizador não encontrado")
            return redirect(request, "login.html")
    else:
        print("request vazio",request)
        return render(request, "login.html")



def logout_view(request):
    #auth.logout(request)
    logout(request)



def registar(request):
    if request.method == "POST":
        user = User.objects.create_user(request.POST["username"],request.POST["email"], request.POST["password"])
        user.save()
        print("Utilizador foi guardado")
        user_authenticate = authenticate(username=user.username, password=request.POST["password"])
        if user_authenticate is not None:
            login(request, user)
            print("User iniciou sessão",user)
        else:
            print("User NÂO iniciou sessão",user)
    return render(request, "registar.html")


def home(request=None):
    return 

def addCarteira(request = None):
    print("REQUEST--)",request.POST)
    user = User.objects.get(username=request.user)
    carteira = Carteira(saldo=request.POST["saldo_carteira"],
    data = "falta codigo para data",
    user = user)#.save()

    return render(request, "home.html",{"user": user})

def getCarteiras(request= None):
    user = User.objects.get(username=request.user)
    carteiras = Carteira.objects.filter(user=user)
    carteiras_json = []
    for i in carteiras:
        carteiras_json += i.nome
    return JsonResponse({"message":"OK","carteiras":carteiras_json})   

def addTransacao(request = None):
    print("REQUEST--)",request.POST)
    user = User.objects.get(username=request.user)
    carteira = Carteira.objects.filter(user=user) # tens de encontrar a carteira que vem no request
    print("len user: ",user, "len Carteira: ", len(carteira))
    #adicionar os valores do request a uma nova instancia da class Transacao_Carteira e fazer .save()
    #tens de subtrair do teu saldo atual o preco que user pagou, guardar novo valor do saldo sendo este um many to one
    Transacao_Carteira(descricao=request.POST["descricao"],
    data = "falta codigo para data",
    valor_pago = request.POST["txt_custo"],
    quantidade= request.POST["txt_quantidade"],
    carteira = carteira)

def transacoesRecentesJson(request = None):
    print("request-)",request.POST)
    user = User.objects.get(username=request.user)
    carteira = Carteira.objects.filter(user=user)

    transacoes = Transacao_Carteira.objects.filter(
        descricao = request.POST["descricao"],
        valor_pago = request.POST["valor_pago"],
        categoria = request.POST["categoria"],
        quantidade = request.POST["quantidade"],
        data = request.POST["data"], # vais ter de substituir 
        carteira= carteira).save()
    print("len user: ", len(user), "len Carteira: ", len(carteira), "len transacoes: ", len(transacoes))
    

def balancoJson(request= None):
    #aqui queres compor os dados para um grafico onde vais ver as datas e o dinheiro que tinhas nessa data
    print("REQ",request.POST)

def historicoFincanceiroJson(request= None):
    print("REQ",request.POST)

def historicoGastosJson(request= None):
    print("REQ",request.POST)

def agendamentosGastosJson(request= None):
    print("REQ",request.POST)

