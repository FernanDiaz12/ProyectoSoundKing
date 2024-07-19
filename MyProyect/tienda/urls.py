from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('piano',views.piano),
    path('bateria',views.bateria),
    path('acustica',views.acustica),
    path('electrica',views.electrica),
    path('login',views.login),
    path('carrito',views.carrito),
]