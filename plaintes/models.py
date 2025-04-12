from django.db import models
from tinymce import models as tinymce_models

# Create your models here.


class Faq(models.Model):
    question = models.CharField(max_length=255, unique=True)
    reponse = tinymce_models.HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)


class glossaire(models.Model):
    mot = models.CharField(max_length=255, unique=True)
    definition = tinymce_models.HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

class traitement(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre


class plainte(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=255)
    objet = models.CharField(max_length=255)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    traitement = models.ForeignKey(traitement, on_delete=models.CASCADE, default=1)