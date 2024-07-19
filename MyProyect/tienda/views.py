from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "tienda/SoundKing.html", {})

def piano(request):
    return render(request, "tienda/Piano.html", {})

def bateria(request):
    return render(request, "tienda/Bateria.html", {})

def acustica(request):
    return render(request, "tienda/GuitarraAcustica.html", {})

def electrica(request):
    return render(request, "tienda/GuitarraElectrica.html", {})

def login(request):
    return render(request, "tienda/Login.html", {})

def carrito(request):
    return render(request, "tienda/Carrito.html", {})