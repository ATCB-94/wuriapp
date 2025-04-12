from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index),
    path('ressources-documentaire.html', views.document),
    path('publication-media.html', views.pub_media),
    path('gallerie-activites.html', views.activite),
    path('videos-activites.html', views.videos_activite),
    path('videos-gallerie.html', views.videos_activite),
    path('gallerie-activites/<libele>', views.gallerie),
    path('videos-activites/<id>', views.videos),
]
