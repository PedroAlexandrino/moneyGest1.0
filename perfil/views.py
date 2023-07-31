from django.shortcuts import render

# Create your views here.
def main(request):
    print("entrou no main")
    return render(request, "home.html")