from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('presentation/', views.index),
    path('presentation/mot-du-coordinateur/', views.mot_du_coordinateur),
    path('presentation/mot-du-ministre/', views.mot_du_ministre),
    path('presentation/composant-01/', views.composant_01),
    path('presentation/composant-02/', views.composant_02),
    path('presentation/composant-03/', views.composant_03),
]
