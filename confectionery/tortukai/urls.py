from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('uzsakymai', views.order, name = "order"),
    path('apie', views.about, name = "about")
]