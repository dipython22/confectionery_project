from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from .models import Cake, Client, Occasion, Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CakeReviewForm
from django.db.models import Q


@csrf_protect
def register(request):
    if request.method == "POST":
        # duomenu surinkimas
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # validuosim forma, tikrindami ar sutampa slaptažodžiai, ar egzistuoja vartotojas
        error = False
        if not password or password != password2:
            messages.error(request, 'Slaptažodžiai nesutampa.')
            error = True
        if not username or User.objects.filter(username=username).exists():
            messages.error(request, f'Vartotojas {username} jau egzistuoja.')
            error = True
        if not email or User.objects.filter(email=email).exists():
            messages.error(request, f'Vartotojas su el.paštu {email} jau egzistuoja.')
            error = True
        if error:
            return redirect('register')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, f'Vartotojas {username} užregistruotas sėkmingai. Galite prisijungti')
            return redirect('home')
    return render(request, 'tortukai/register.html')

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


class CakeDetailView(generic.DetailView, FormMixin):
    model = Cake
    template_name = 'tortukai/cake.html'
    form_class = CakeReviewForm

    def get_success_url(self):
        return reverse('cake', kwargs={'pk': self.object.id })
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.cake = self.object
        form.instance.subscriber = self.request.user
        form.save()
        return super().form_valid(form)


class Ordered_cake_by_user(LoginRequiredMixin, generic.ListView):
    model = Order
    context_object_name = 'order_list' 
    template_name = 'tortukai/user_orders_list.html'
    paginate_by = 4

    def get_queryset(self):
        return super().get_queryset().filter(customer=self.request.user).filter(Q(status__exact='u') | Q(status__exact='p')).order_by('deadline')



