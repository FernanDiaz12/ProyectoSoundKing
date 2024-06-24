from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def administracion(request):
    return HttpResponse("<h1> Administración </h1>")