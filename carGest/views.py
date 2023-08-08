from django.shortcuts import render

# Create your views here.
def carGest(request):
    print("entrou no carGest")
    return render(request, "home_car.html")