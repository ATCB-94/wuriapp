
from django.contrib import admin
from django.urls import path, include
from actualites import views
from presentation import views
from ressources import views
from plaintes import views
from offres import views
from .veiws import index, contact, gallerie, atelier_regional_des_projets_WURI_6_7_et_8_mai2024

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('gallerie/', gallerie),
    path('atelier_regional_des_projets_WURI_6_7_et_8_mai2024/', atelier_regional_des_projets_WURI_6_7_et_8_mai2024),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('actualites', include("actualites.urls")),
    path('', include("presentation.urls")),
    path('ressources/', include("ressources.urls")),
    path('plaintes/', include("plaintes.urls")),
    path('offres/', include("offres.urls")),
]
