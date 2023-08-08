from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
def main(request):
    print("entrou no main")
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def registar(request):
    return render(request, "registar.html")

=======

def home(request=None):
    return 
>>>>>>> 77691f076a59c88abdd78764058117470b18979e
