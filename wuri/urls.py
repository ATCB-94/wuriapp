
from django.contrib import admin
from django.urls import path, include
from actualites import views
from presentation import views
from .veiws import index, contact, gallerie, atelier_regional_des_projets_WURI_6_7_et_8_mai2024

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('gallerie/', gallerie),
    path('atelier_regional_des_projets_WURI_6_7_et_8_mai2024/', atelier_regional_des_projets_WURI_6_7_et_8_mai2024),
    path('admin/', admin.site.urls),
    path('actualites', include("actualites.urls")),
    path('', include("presentation.urls"))
]
