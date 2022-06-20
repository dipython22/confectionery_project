from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "tortukai/index.html")

def order(request):
    return render(request, "tortukai/orders.html")

# Create your views here.
