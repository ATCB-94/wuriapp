from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('recrutement.html', views.recrutement),
    path('appels-offres.html', views.appelsOffres),
    path('ami.html', views.ami),
]
