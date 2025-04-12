from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

class AppelsOfrres(models.Model):
    titre = models.CharField(max_length=255)
    document = models.FileField(upload_to='plaintes/appelsOffres', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)


class AMI(models.Model):
    titre = models.CharField(max_length=255)
    document = models.FileField(upload_to='offres/ami', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)


class Contrat(models.Model):
    libele = models.CharField(max_length=255)

    def __str__(self):
        return self.libele

class Recrutement(models.Model):
    titre = models.CharField(max_length=255)
    mission = tinymce_models.HTMLField(null=True)
    niveau_etude = models.CharField(max_length=150)
    niveau_experience = models.CharField(max_length=255)
    contrat_propose = models.ForeignKey(Contrat, on_delete=models.CASCADE, related_name='contrat_recrutementt')
    competences_cles = models.CharField(max_length=255)