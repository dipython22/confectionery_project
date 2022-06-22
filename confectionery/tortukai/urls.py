from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('uzsakymai', views.order, name = "order"),
    path('apie', views.about, name = "about"),
    path('cakes/', views.cakes, name='cakes'),
    path('cake/<int:cake_id>/', views.cake, name='cake'),
]