from django.shortcuts import render

# Create your views here.
def main(request):
    print("entrou no main")
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def registar(request):
    return render(request, "registar.html")


def home(request=None):
    return 
