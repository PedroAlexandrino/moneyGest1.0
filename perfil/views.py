from django.shortcuts import render, redirect
from perfil.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import auth

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
