from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('faq.html', views.faq, name='faq'),

    path('soumettre-une-requette.html', views.soumettre_une_requette),
    path('add_plainte', views.add_plainte, name='add_plainte'),
    path('create', views.plainte_create_view, name='create'), 

    path('suivi-plainte.html', views.suivi_plainte, name='suivi_plainte'),
    path('recherche', views.recherche, name='recherche'),
    #path('recherche-plainte.html', views.recherche_plainte, name='recherche-plainte'),

    #GLOSSAIRE
    path('glossaire.html', views.glassaire, name='glossaire'),
    path('rech_glossaire', views.rech_glossaire, name='rech_glossaire'),
]
