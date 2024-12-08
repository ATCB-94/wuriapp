from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home),
    path('/home/', views.index),
    path('/<int:id>/', views.detail, name="post_detail"),
]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
