from django.shortcuts import render


def home(request):
    return render(request, "tortukai/home.html")

def order(request):
    return render(request, "tortukai/orders.html")

def about(request):
    return render(request, "tortukai/about.html")

# Create your views here.
