from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Cake, Client, Occasion, Order



def home(request):
    return render(request, "tortukai/home.html")

def order(request):
    return render(request, "tortukai/orders.html")

def about(request):
    return render(request, "tortukai/about.html")

# Create your views here.
def cakes(request):
    cakes = Cake.objects.all()
    return render(request, 'tortukai/cakes.html', {'cakes': cakes})

def cake(request, cake_id):
    cake = get_object_or_404(Cake, pk=cake_id)
    return render(request, 'tortukai/cake.html', {'cake': cake})
